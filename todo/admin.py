from distutils.command import register
from django.contrib import admin
from .models import Todo

admin.site.register(Todo)