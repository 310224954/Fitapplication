from django.contrib import admin

#New models for admin view
from .models import Products, Meals




admin.site.register(Products)
admin.site.register(Meals)



