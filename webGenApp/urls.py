from django.conf.urls import url
from webGenApp import views

urlpatterns=[
    url(r'^$', views.index,name='index')
]
