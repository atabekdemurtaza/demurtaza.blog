from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'active']
    list_filter = ['name', 'description', 'active']
    list_editable = ['active',]
