from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^destroy/(?P<id>[0-9]+)$', views.show_destroy),
    url(r'^comment/(?P<id>[0-9]+)$', views.show_comments),
    url(r'^(?P<id>[0-9]+)/destroy', views.destroy),
    url(r'^new_comment$', views.new_comment),
    url(r'^delete_comment/(?P<id>[0-9]+)$', views.delete_comment),
]
