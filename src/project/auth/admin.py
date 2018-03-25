from django.contrib import admin

from project.auth.helpers import hide_key
from project.auth.models import AccessKey


@admin.register(AccessKey)
class AccessKeyAdmin(admin.ModelAdmin):
    list_display = ('hidden_key', 'user')

    def hidden_key(self, obj):
        return hide_key(obj.key)

    hidden_key.short_description = 'Key'
