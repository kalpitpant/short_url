from django.shortcuts import render, redirect

# Create your views here.

from django.urls import reverse
from tinyurl.models import ShortURL
from django.http import HttpResponse , HttpResponseRedirect, HttpResponsePermanentRedirect

def index(request):
    request_path = request.path
    request_path = request_path.replace('/' , '')
    
    original_web_url = ShortURL.objects.filter(shortcut_url = request_path).values() 
    if original_web_url.count():
        original_web_url = original_web_url[0]['original_website']
        
        return redirect(original_web_url)
    else:
        return render(request , 'tinyurl/index.html')

    