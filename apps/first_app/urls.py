from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^success$', views.success), #reg/log should go to this page 
	url(r'^item/(?P<wish_id>\d+)$', views.item),
	url(r'^additem$', views.additem),
	url(r'^saveitem$', views.saveitem),
	url(r'^add_wish/(?P<wish_id>\d+)$', views.add_wish),
	url(r'^remove/(?P<wish_id>\d+)$', views.remove),
	url(r'^delete/(?P<wish_id>\d+)$', views.delete),
]