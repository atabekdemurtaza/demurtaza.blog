from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings


class StreamPlatform(models.Model):
    name = models.CharField(_('name'), max_length=30)
    about = models.CharField(_('about'), max_length=30)
    url = models.URLField(_('url'), max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Stream Platforms'
        verbose_name = 'Stream Platform'


class MovieList(models.Model):

    GENRE_CHOICES = (
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('history', 'History')
    )
    title = models.CharField(_('name'), max_length=100, blank=True, null=True)
    storyline = models.TextField(_('description'), blank=True, null=True)
    platform = models.ForeignKey(
        to=StreamPlatform,
        verbose_name=_('platform'),
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='watchlist'
    )
    active = models.BooleanField(
        _('active'),
        default=True,
        blank=True,
        null=True)
    genre = models.CharField(
        _('genre'),
        choices=GENRE_CHOICES,
        max_length=20,
        null=True,
        blank=True
    )
    poster = models.ImageField(
        _('poster'),
        upload_to='movie_posters/',
        null=True,
        blank=True
    )
    trailer_url = models.URLField(_('trailer URL'), null=True, blank=True)
    director = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='directed_movies',
        verbose_name=_('director')
    )
    cast = models.ManyToManyField(
        User,
        related_name='acted_in_movies',
        verbose_name=_('cast'),
    )
    created = models.DateTimeField(
        _('created'),
        auto_now_add=True,
        blank=True,
        null=True
    )
    release_date = models.DateField(
        _('release date'),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Movies'
        verbose_name = 'movie'


class Review(models.Model):
    review_user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name=_('user'),
        blank=True,
        null=True
    )
    rating = models.PositiveIntegerField(
        _('rating'),
    )
    description = models.TextField(
        _('description'),
        blank=True,
        null=True
    )
    created = models.DateTimeField(
        _('created'),
        auto_now_add=True
    )
    updated = models.DateTimeField(
        _('updated'),
        auto_now=True
    )
    active = models.BooleanField(_('active'), default=True)
    watchlist = models.ForeignKey(
        to=MovieList,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    def __str__(self) -> str:
        return f'{self.watchlist.title} with {self.rating}'
