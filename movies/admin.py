from django.contrib import admin
from .models import MovieList, StreamPlatform


@admin.register(MovieList)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'storyline', 'active']
    list_filter = ['title', 'active']
    list_editable = ['active',]
    search_fields = ['title']


@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ['name', 'about', 'url']
    search_fields = ['name']
