from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from project.projects.models import Project


def project_file(request, project_code, file_path='index.html'):
    project = get_object_or_404(Project, code=project_code)
    user = request.user

    if not user.is_authenticated or user not in project.users.all():
        return redirect_to_login(request.get_full_path(), 'project_auth:access')

    vault_root = settings.VAULT_ROOT.rstrip('/')
    response = HttpResponse()

    # The actual file will be served by HTTP server.
    response['X-Accel-Redirect'] = f'{vault_root}/{project_code}/{file_path}'

    return response
