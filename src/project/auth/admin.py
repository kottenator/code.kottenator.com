from django.contrib import admin

from project.auth.helpers import hide_key
from project.auth.models import AccessKey


def partial_hidden_key(obj):
    return hide_key(obj.key)


partial_hidden_key.short_description = 'Key'


@admin.register(AccessKey)
class AccessKeyAdmin(admin.ModelAdmin):
    list_display = (partial_hidden_key, 'user')
