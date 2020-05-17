from django.urls import path, re_path, include
from . import views

app_name='blog'

#urlpatterns = [
#	path('', views.index, name = "index"),
#	path('post/(<slugInput>[\w-]+)/', views.detailPost),
#	path('category/(<categoryInput>[\w-]+)/', views.categoryPost),
#]

urlpatterns = [
	re_path(r'^$', views.index, name = "index"),
	re_path(r'^post/(?P<slugInput>[\w-]+)/$', views.detailPost, name = "detailPost"),
	re_path(r'^category/(?P<categoryInput>[\w-]+)/$', views.categoryPost, name = "categoryPost"),
]