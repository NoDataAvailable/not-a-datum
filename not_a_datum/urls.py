from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'not_a_datum.views.home', name='home'),
    # url(r'^not_a_datum/', include('not_a_datum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'not_a_datum.views.home'),  
    url(r'^hello/$', 'not_a_datum.views.hello'),  
    url(r'^submit/$', 'not_a_datum.views.submit'),  
)

