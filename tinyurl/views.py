from django.shortcuts import render

# Create your views here.
from .models import ShortURL
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from .form import InputForm
from django.urls import reverse
from .hash import fnv1a_32

def index(request):
    context = {}
    context['form'] = InputForm
    return render(request , 'tinyurl/index.html' , context)


def getURL(request):
    form = InputForm(request.POST)

    original_url = request.POST['url_to_short']
    short_url = getHashValue(original_url)
    
    
    instance = ShortURL(original_website = original_url , shortcut_url = short_url)
    instance.save()

    
    domain_name = 'http://127.0.0.1:8000'
    new_url = f'{domain_name}/{short_url}'
    
    context = {}
    context['original_url'] = original_url
    context['short_url'] = new_url

    return render(request , 'tinyurl/index.html' , context)

def getHashValue(original_url):
    short_url = hex(fnv1a_32(str.encode(original_url)))
    return short_url


def convertURL(request):
    short_url = request.session['short_url']
    return HttpResponse(f"Your tiny url will be http://127.0.0.1:8000/{short_url}")