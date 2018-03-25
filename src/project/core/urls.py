from django.urls import path

from .views import home_page, bad_request, permission_denied, page_not_found, server_error

urlpatterns = [
    path('', home_page),

    # Sample error pages.
    path('400/', bad_request),
    path('403/', permission_denied),
    path('404/', page_not_found),
    path('500/', server_error)
]
