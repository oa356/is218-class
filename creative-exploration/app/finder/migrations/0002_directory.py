from django.db import migrations


def seed(apps, schema_editor):
    Service = apps.get_model("finder", "Service")
    entries = [
        ("Commuter Café", "Dining", "Union, room 110"),
        ("Commuter Lounge", "Study", "Union, room 112"),
        ("Math Tutoring", "Academic support", "Learning Center, room 201"),
        ("Transit Desk", "Transportation", "Welcome Hall, room 104"),
        ("Writing Center", "Academic support", "Learning Center, room 205"),
    ]
    for name, category, location in entries:
        Service.objects.create(name=name, category=category, location=location)


class Migration(migrations.Migration):
    dependencies = [("finder", "0001_initial")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
