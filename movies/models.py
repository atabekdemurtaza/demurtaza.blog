from django.db import models
from django.utils.translation import gettext_lazy as _


class StreamPlatform(models.Model):
    name = models.CharField(_('name'), max_length=30)
    about = models.CharField(_('about'), max_length=30)
    url = models.URLField(_('url'), max_length=30)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Streams'
        verbose_name = 'stream'


class MovieList(models.Model):
    title = models.CharField(_('name'), max_length=25)
    storyline = models.TextField(_('description'))
    active = models.BooleanField(_('active'), default=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Movies'
        verbose_name = 'movie'
