
from django.conf.urls import patterns, include, url
from app import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index/$', views.index, name='index'),
	url(r'^option2/$', views.option2, name='option2'),
	url(r'^north/$', views.north, name='north'),
	url(r'^need_delivery/$', views.need_delivery, name='need_delivery'),
	url(r'^i_donated/$', views.i_donated, name='i_donated'),
	url(r'^received_water/$', views.received_water, name='received_water'),
	url(r'^service/$', views.service, name='service'),
	url(r'^want_to_donate/$', views.want_to_donate, name='want_to_donate'),
	url(r'^want_to_volunteer/$', views.want_to_volunteer, name='want_to_volunteer'),
	url(r'^we_will_distribute/$', views.we_will_distribute, name='we_will_distribute')
]
