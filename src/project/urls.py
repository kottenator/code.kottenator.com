from django.contrib import admin
from django.urls import path, include

import project.auth.urls
import project.core.urls
from project.core.views import bad_request, permission_denied, page_not_found, server_error
import project.projects.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include(project.projects.urls)),
    path('', include(project.auth.urls)),
    path('', include(project.core.urls))
]


handler400 = bad_request
handler403 = permission_denied
handler404 = page_not_found
handler500 = server_error
