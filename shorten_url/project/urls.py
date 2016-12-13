from django.conf.urls import url
from django.contrib import admin

from shortener.views import HomeView, LogoutView, RedirectURLView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'(?P<shortcode>[\w-]+)/$', RedirectURLView.as_view(), name='shortcode')
]
