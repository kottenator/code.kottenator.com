from django.contrib import admin
from django.urls import path, include

import project.auth.urls
import project.core.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(project.auth.urls)),
    path('', include(project.core.urls))
]
