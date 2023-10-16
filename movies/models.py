from django.db import models
from django.utils.translation import gettext_lazy as _


class Movie(models.Model):
    name = models.CharField(_('name'), max_length=25)
    description = models.TextField(_('description'))
    active = models.BooleanField(_('active'), default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
