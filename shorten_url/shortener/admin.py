from django.contrib import admin

# Register your models here.
from .models import MyShortURL

admin.site.register(MyShortURL)