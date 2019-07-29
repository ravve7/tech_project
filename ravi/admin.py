from django.contrib import admin

# Register your models here.
from .models import Products,inventory
admin.site.register(Products)
admin.site.register(inventory)