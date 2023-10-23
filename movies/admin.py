from django.contrib import admin
from .models import MovieList, StreamPlatform, Review
from django import forms
from django.core.exceptions import ValidationError


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


class ReviewAdminForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 5:
            raise ValidationError('Rating must be between 1 and 5.')
        return rating


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ['rating', 'created', 'updated', 'watchlist']
    search_fields = ['created']
