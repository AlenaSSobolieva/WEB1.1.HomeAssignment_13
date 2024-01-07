# quoteapp/admin.py

from django.contrib import admin

from django.contrib import admin
from quoteproject.quoteapp.models import Author, Quote

admin.site.register(Author)
admin.site.register(Quote)

