from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from project.projects.models import Project


def project_file(request, project_code, file_path='index.html'):
    project = get_object_or_404(Project, code=project_code)
    user = request.user

    if not user.is_authenticated or user not in project.users.all():
        return redirect_to_login(request.get_full_path(), 'project_auth:access')

    response = HttpResponse()
    response['X-Accel-Redirect'] = f'src/vault/{project_code}/{file_path}'

    return response
