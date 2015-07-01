from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'testdoc.views.home', name='home'),
    url(r'^blog$', 'testdoc.views.blog', name='blog'),
    url(r'^userauth/', include('userauth.urls')),
    url(r'^groups/', include('groups.urls')),
    url(r'^myprofile/', include('myprofile.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
