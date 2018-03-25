from django.contrib import admin

from project.projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'get_users')
    filter_horizontal = ('users',)

    def get_users(self, obj):
        return ", ".join([u.username for u in obj.users.all()]) or '(public)'

    get_users.short_description = 'Users'
