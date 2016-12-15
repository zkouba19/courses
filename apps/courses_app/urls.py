from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^process/$', views.process),
    url(r'^remove/(?P<id>\d*)$', views.remove),
    url(r'^remove/(?P<id>\d*)/delete$', views.delete), 
    url(r'^remove/(?P<id>\d*)/go_back/$', views.go_back),
]
