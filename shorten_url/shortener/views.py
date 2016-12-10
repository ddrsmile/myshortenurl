from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import MyShortURL

class MyShortURLView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(MyShortURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)