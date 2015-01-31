__author__ = 'ptrollins'

from django.conf.urls import patterns, include, url
from django.contrib import admin
# from dashboard import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'dashboard.views.index'),
    # url(r'^index.html', 'dashboard.views.index'),
    url(r'^upload$', 'dashboard.views.upload_file'),
    url(r'^display$', 'dashboard.views.display_data'),
)
