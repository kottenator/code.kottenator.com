from django.conf import settings
from django.db import models

from project.auth.helpers import hide_key


class AccessKey(models.Model):
    key = models.CharField(max_length=256, unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'<AccessKey {hide_key(self.key)} - {self.user}>'
