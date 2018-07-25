from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^(?P<inputString>.*)/$', views.getEntityResponse, name='getEntityResponse'),
]


