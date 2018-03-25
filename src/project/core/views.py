from django.shortcuts import render


def home_page(request):
    return render(request, 'core/home-page.html')


def bad_request(request, exception=None):
    return render(request, 'core/400.html', status=400)


def permission_denied(request, exception=None):
    return render(request, 'core/403.html', status=403)


def page_not_found(request, exception=None):
    return render(request, 'core/404.html', status=404)


def server_error(request):
    return render(request, 'core/500.html', status=500)
