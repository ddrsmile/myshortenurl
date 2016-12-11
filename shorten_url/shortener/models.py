from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse_lazy

from .utils import code_generator, create_shortcode

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)

class MyShortURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(MyShortURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs    

class MyShortURL(models.Model):
    url = models.URLField(max_length=255)
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = MyShortURLManager()

    def save(self, *args, **kwargs):
        if not self.shortcode:
            self.shortcode = create_shortcode(self)
        super(MyShortURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)