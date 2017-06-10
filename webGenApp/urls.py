from django.conf.urls import url
from webGenApp import views

urlpatterns=[
    url(r'^$', views.index,name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^([A-Za-z]{3,})/', views.test, name='test'),
    url(r'^([0-9]{1,2})$', views.index1, name='index'),

]
