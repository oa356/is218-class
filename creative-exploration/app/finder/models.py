from django.conf import settings
from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=80, unique=True)
    category = models.CharField(max_length=40)
    location = models.CharField(max_length=100)


class Bookmark(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    saved = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["owner", "service"], name="one_save_per_service")]
