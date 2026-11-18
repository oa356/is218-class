from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from .models import Bookmark, Service
from .search import clean, literal, lookup, suggestions


class SearchTrial(TestCase):
    def test_strategy_against_conditional(self):
        services = list(Service.objects.order_by("name"))
        cases = [
            ("commuter", ["Commuter Café", "Commuter Lounge"]), (" ACADEMIC SUPPORT ", ["Math Tutoring", "Writing Center"]),
            ("cafe\u0301", ["Commuter Café"]), ("transit", ["Transit Desk"]),
            ("trasnit", ["Transit Desk"]), ("writng", ["Writing Center"]), ("lounje", ["Commuter Lounge"]),
            ("tutroing", ["Math Tutoring"]), ("comuter cafe", ["Commuter Café"]),
            ("zebra", []), ("volcano", []), ("jazz", []),
        ]
        for index, (query, expected) in enumerate(cases):
            with self.subTest(query=query):
                key = clean(query)
                direct = literal(key, services)
                baseline = ("Results", direct)
                if not direct:
                    fallback = suggestions(key, services)
                    if fallback:
                        baseline = ("Possible matches", fallback)
                label, hits = lookup(query, services)
                self.assertEqual((label, hits), baseline)
                names = [item.name for item in hits]
                if 4 <= index < 9:
                    self.assertEqual(label, "Possible matches")
                    self.assertIn(expected[0], names[:3])
                else:
                    self.assertEqual(names, expected)


class AccountJourney(TestCase):
    password = "Riverbed-Sample-932"

    @classmethod
    def setUpTestData(cls):
        cls.a = get_user_model().objects.create_user("commuter_a", password=cls.password)
        cls.b = get_user_model().objects.create_user("commuter_b", password=cls.password)
        cls.service = Service.objects.get(name="Transit Desk")
        cls.save_url = f"/save/{cls.service.pk}/"

    def test_registration_and_credentials(self):
        fields = {"username": "new_student", "password1": self.password, "password2": self.password}
        self.assertRedirects(self.client.post("/signup/", fields), "/login/")
        self.assertContains(self.client.post("/signup/", fields), "already exists")
        self.assertContains(self.client.post("/login/", {"username": "new_student", "password": "wrong"}), "correct username")
        self.assertRedirects(self.client.post("/login/", {"username": "new_student", "password": self.password}), "/")

    def test_repeat_save_and_private_dashboard(self):
        self.client.force_login(self.a)
        for _ in range(2):
            self.client.post(self.save_url, {"owner": self.b.pk})
        self.assertEqual(Bookmark.objects.filter(owner=self.a).count(), 1)
        self.client.logout()
        self.client.force_login(self.b)
        self.assertContains(self.client.get("/"), "No bookmarks yet")
        self.assertNotContains(self.client.get("/", {"owner": self.a.pk}), "Transit Desk")
        self.client.logout()
        self.client.force_login(self.a)
        self.assertContains(self.client.get("/"), "Your bookmarks (1)")

    def test_blank_unknown_and_save_method(self):
        self.client.force_login(self.a)
        self.assertContains(self.client.get("/", {"q": "   "}), "Enter a service name")
        self.assertEqual(self.client.get(self.save_url).status_code, 405)
        self.assertEqual(self.client.post("/save/987654/").status_code, 404)
        self.assertFalse(Bookmark.objects.exists())

    def test_csrf_and_logout_revocation(self):
        client = Client(enforce_csrf_checks=True)
        client.force_login(self.a)
        self.assertEqual(client.post(self.save_url).status_code, 403)
        client.get("/")
        stale = Client()
        stale.cookies["sessionid"] = client.cookies["sessionid"].value
        client.post("/logout/", {"csrfmiddlewaretoken": client.cookies["csrftoken"].value})
        self.assertRedirects(stale.get("/"), "/login/?next=/")
        self.assertEqual(stale.post(self.save_url).status_code, 302)
        self.assertFalse(Bookmark.objects.exists())

    def test_name_and_password_sessions(self):
        self.client.force_login(self.a)
        other = Client()
        other.force_login(self.a)
        self.client.post("/account/", {"display_name": "Avery", "owner": self.b.pk})
        self.assertContains(self.client.get("/"), "Signed in as Avery")
        self.b.refresh_from_db()
        self.assertEqual(self.b.first_name, "")
        fields = {"old_password": "wrong", "new_password1": "BlueSample-942!", "new_password2": "BlueSample-942!"}
        self.assertContains(self.client.post("/password/", fields), "incorrectly")
        fields["old_password"] = self.password
        self.assertRedirects(self.client.post("/password/", fields), "/")
        self.assertEqual(other.get("/").status_code, 302)
        self.assertFalse(other.login(username=self.a.username, password=self.password))
        self.assertTrue(other.login(username=self.a.username, password=fields["new_password1"]))
