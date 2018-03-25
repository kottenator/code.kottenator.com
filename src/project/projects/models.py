from django.conf import settings
from django.db import models


class Project(models.Model):
    code = models.CharField(max_length=128)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return f'<Project code:{self.code}>'
