from django.contrib import admin
from django.urls import path, include

import project.core.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(project.core.urls))
]
