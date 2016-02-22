
from django.conf.urls import patterns, include, url
from api import views

urlpatterns = [
    url(r'^locations/$', views.locations, name='locations'),
]