from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import MyShortURL
from analytics.models import ClickEvent
from .forms import SubmitURLForm

class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitURLForm()
        context = {
            'form' : form,
        }
        return render(request, 'shortener/home.html', context)
    
    def post(self, request, *args, **kwargs):
        form = SubmitURLForm(request.POST)
        context = {'form' : form}
        template = 'shortener/home.html'

        user = request.user
        if not user.is_authenticated:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

        if user:
            login(request, user)
        else:
            context['emsg'] = "You must have an account to use this URL shortener!!"
            return render(request, template, context)

        if form.is_valid():
            url = form.cleaned_data.get('url')
            obj, created = MyShortURL.objects.get_or_create(url=url)
            if created:
                ClickEvent.objects.create(my_url=obj)
            short_url = request.build_absolute_uri(obj.shortcode)
            click_count = obj.clickevent.count
            context = {'origin_url': url, 'short_url': short_url, 'click_count' :click_count, 'form': SubmitURLForm()}
            template = 'shortener/url.html'
        return render(request, template, context)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')

class RedirectURLView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(MyShortURL, shortcode=shortcode)
        print("shortcode '{0}' with {1} access count".format(shortcode, ClickEvent.objects.create_event(obj)))
        return HttpResponseRedirect(obj.url)