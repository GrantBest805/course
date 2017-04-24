from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process', views.show),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^clear/(?P<id>\d+)$', views.clear),


]
