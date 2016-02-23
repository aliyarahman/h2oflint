
from django.conf.urls import patterns, include, url
from app import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login_view'),  
    url(r'^logout/$', views.logout_view, name='logout_view'),      
	url(r'^request_delivery/$', views.request_delivery, name='request_delivery'),
    url(r'^edit_request_delivery/$', views.edit_request_delivery, name='edit_request_delivery'),
	url(r'^organization_offer/$', views.organization_offer, name='organization_offer'),
	url(r'^individual_offer/$', views.individual_offer, name='individual_offer'),
    url(r'^search/$', views.search, name='search'),
    url(r'^request_received/$', views.request_received, name='request_received'),
    url(r'^changes_updated/$', views.changes_updated, name='changes_updated'),
    url(r'^edit_organization/$', views.edit_organization, name='edit_organization'),
    url(r'^edit_individual/$', views.edit_individual, name='edit_individual'),
    url(r'^add_another_help_offer/$', views.add_another_help_offer, name='add_another_help_offer'),
    url(r'^about/$', views.about, name='about'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^data/$', views.data, name='data'),
    url(r'^register/$', views.register, name='register'),
]