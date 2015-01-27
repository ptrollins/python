__author__ = 'ptrollins'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from dashboard import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    # url(r'^index.html', views.index),
    url(r'^upload.html$', views.upload_file),
    url(r'^scores.html$', views.scores),
)
