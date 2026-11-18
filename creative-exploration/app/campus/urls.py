from django.contrib.auth import views as auth
from django.urls import path, reverse_lazy
from finder import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", auth.LoginView.as_view(template_name="form.html", extra_context={"heading": "Sign in"}), name="login"),
    path("logout/", auth.LogoutView.as_view(), name="logout"),
    path("save/<int:pk>/", views.save, name="save"),
    path("account/", views.account, name="account"),
    path("password/", auth.PasswordChangeView.as_view(template_name="form.html", success_url=reverse_lazy("home"),
                                                     extra_context={"heading": "Change password"}), name="password"),
]
