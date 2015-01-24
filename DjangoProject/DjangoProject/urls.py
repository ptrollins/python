from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^$', 'DjangoProject.views.home'),
    # Examples:
    # url(r'^$', 'DjangoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    )

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )


