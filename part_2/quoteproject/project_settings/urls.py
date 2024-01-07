# project_settings/urls.py

import os
from django.urls import path, include  # Add this import
from django.core.wsgi import get_wsgi_application
from django.contrib import admin

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quoteproject.project_settings.settings")
application = get_wsgi_application()


urlpatterns = [
    path("admin/", admin.site.urls),
    path('templates/author_quote/', include('quoteproject.quoteapp.urls')),  # Include the quoteapp URLs
    # Add other URL patterns as needed
]
