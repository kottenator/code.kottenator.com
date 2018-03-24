from django.urls import path

from .views import AccessPage

app_name = 'project_auth'

urlpatterns = [
    path('access/', AccessPage.as_view(), name='access'),
]
