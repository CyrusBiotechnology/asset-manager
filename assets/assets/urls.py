from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'assets.views.index', name='index'),

    url(r'^se', 'assets.views.ajax_search', name='ajax_search'),

    url(r'^assets/new', 'assets.views.create_asset', name='create_asset'),
    url(r'^assets/$', 'assets.views.asset', name='asset_alias'),
    url(r'^assets/(?P<aID>[0-9]+)/?$', 'assets.views.asset', name='asset'),
    url(r'^assets/(?P<aID>[0-9]+)/edit/?', 'assets.views.edit_asset', name='edit_asset'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
