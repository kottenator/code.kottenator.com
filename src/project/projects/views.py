from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import never_cache

from project.projects.models import Project


@never_cache
def project_file(request, project_code, file_path='index.html'):
    project = get_object_or_404(Project, code=project_code)
    user = request.user
    allowed_users = project.users.all()

    if allowed_users and user not in allowed_users:
        return redirect_to_login(request.get_full_path(), 'project_auth:access')

    vault_base_url = settings.VAULT_BASE_URL.rstrip('/')
    response = HttpResponse()

    # The actual file will be served by HTTP server.
    response['X-Accel-Redirect'] = f'{vault_base_url}/{project_code}/{file_path}'

    return response
