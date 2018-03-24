from django.contrib.auth.views import LoginView

from .forms import AccessForm


class AccessPage(LoginView):
    form_class = AccessForm
    template_name = 'auth/access-page.html'
