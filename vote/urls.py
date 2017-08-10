from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^video/$', views.video),
    url(r'^outandent/$', views.outandent),
    # url(r'^candidate/(?P<name>[-\w]+)$', views.detail),
]
