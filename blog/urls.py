from django.urls import path, re_path, include
from . import views

urlpatterns = [
	re_path(r'^$', views.index),
	re_path(r'^post/(?P<slugInput>[\w-]+)/$', views.detailPost),
	re_path(r'^category/(?P<categoryInput>[\w-]+)/$', views.categoryPost),
]