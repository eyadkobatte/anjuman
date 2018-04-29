from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^standards$', views.standards),
    url(r'^categories$', views.categories)
]
