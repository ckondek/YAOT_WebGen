from django.conf.urls import url
from webGenApp import views

urlpatterns=[
    url(r'^$', views.index,name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^([A-Za-z]{3,})/', views.test, name='test'),

] 
