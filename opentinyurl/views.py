from django.shortcuts import render

# Create your views here.

from django.urls import reverse

from django.http import HttpResponse , HttpResponseRedirect

def index(request):
    
    return HttpResponse('This is open tiny url section')