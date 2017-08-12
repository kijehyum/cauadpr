from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^video/$', views.video),
    url(r'^outdoor/$', views.outdoor),
    url(r'^entertainment/$', views.entertainment),
    url(r'^exit/$', views.exit),
]
