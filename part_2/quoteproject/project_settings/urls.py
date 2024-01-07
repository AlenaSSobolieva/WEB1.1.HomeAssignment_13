# project_settings/urls.py

import os
from django.urls import path, include
from django.core.wsgi import get_wsgi_application
from django.contrib import admin

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
application = get_wsgi_application()


urlpatterns = [
    path("admin/", admin.site.urls),
    path('quoteapp/templates/author_quote/', include('urls')),
    # Add other URL patterns as needed
]
