from atexit import register
from django.contrib import admin
from .models import all_models

# Register your models here.
for model in all_models:
    admin.site.register(model)