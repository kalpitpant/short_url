from django.urls import path

from . import views

urlpatterns = [
    path('', views.index  , name = 'index'),
    path('urls', views.getURL  , name = 'getURL'),
    path('convert', views.convertURL  , name = 'convertURL'),
]