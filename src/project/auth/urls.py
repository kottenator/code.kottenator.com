from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import AccessPage

app_name = 'project_auth'

urlpatterns = [
    path('access/', AccessPage.as_view(), name='access'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
