from django.urls import path

from .views import project_file

app_name = 'projects'

urlpatterns = [
    path('<str:project_code>/', project_file, name='project-root'),
    path('<str:project_code>/<path:file_path>', project_file, name='project-file'),
]
