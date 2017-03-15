from django.db import models

from shortener.models import MyShortURL

class ClickEventManager(models.Manager):
    def create_event(self, URLInstance):
        if isinstance(URLInstance, MyShortURL):
            obj, created = self.get_or_create(my_url=URLInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    my_url = models.OneToOneField(MyShortURL, related_name='clickevent')
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    objects = ClickEventManager()

    def __str__(self):
        return "{}".format(self.count)