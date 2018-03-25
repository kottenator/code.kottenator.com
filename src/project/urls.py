from django.contrib import admin
from django.urls import path, include

import project.auth.urls
import project.core.urls
import project.projects.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include(project.projects.urls)),
    path('', include(project.auth.urls)),
    path('', include(project.core.urls))
]
