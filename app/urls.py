
from django.conf.urls import patterns, include, url
from app import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index/$', views.index, name='index'),
	url(r'^request_delivery/$', views.request_delivery, name='request_delivery'),
	url(r'^organization_offer/$', views.organization_offer, name='organization_offer'),
	url(r'^individual_offer/$', views.individual_offer, name='individual_offer'),
    url(r'^search/$', views.search, name='search'),
    url(r'^about/$', views.about, name='about'),
    url(r'^faq/$', views.faq, name='faq'),
]