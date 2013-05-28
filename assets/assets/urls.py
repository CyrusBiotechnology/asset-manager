from django.conf.urls import patterns, include, url
from django.contrib import admin


handler404 = 'assets.assets.views.handler404'


from assets.views import *

admin.autodiscover()

# Asset urls
asset_patterns = patterns('assets.views',
    url(r'^$', 'list', {'model': 'asset'}, name='asset_list'),
    url(r'^new/?', 'create_object', {'model': 'asset'}, name='create_asset'),
    url(r'^(?P<ID>[0-9]+)/?$', 'display_object', {'model': 'asset'}, name='asset'),
    url(r'^(?P<ID>[0-9]+)/edit/?', 'edit_object', {'model': 'asset'}, name='edit_asset'),
)

# Location urls
location_patterns = patterns('assets.views',
    url(r'^new/?', 'create_object', {'model': 'location'}, name='create_location'),
    url(r'^new/?', 'create_object', {'model': 'location'}, name='create_location'),
    url(r'^(?P<ID>[0-9]+)/?$', 'display_object', {'model': 'location'}, name='location'),
    url(r'^(?P<ID>[0-9]+)/edit/?', 'edit_object', {'model': 'location'}, name='edit_location'),
)

# Asset make urls
make_patterns = patterns('assets.views',
    url(r'^$', 'dummy', name='make_alias'),
    url(r'^new/?', 'create_object', {'model': 'make'}, name='create_make'),
    url(r'^(?P<ID>[0-9]+)/?$', 'display_object', {'model': 'make'}, name='make'),
    url(r'^(?P<ID>[0-9]+)/edit/?', 'edit_object', {'model': 'make'}, name='edit_make'),
)

# Asset model urls
model_patterns = patterns('assets.views',
    url(r'^$', 'dummy', name='model_alias'),
    url(r'^new/?', 'create_object', {'model': 'model'}, name='create_model'),
    url(r'^(?P<ID>[0-9]+)/?$', 'display_object', {'model': 'model'}, name='model'),
    url(r'^(?P<ID>[0-9]+)/edit/?', 'edit_object', {'model': 'model'}, name='edit_model'),
)

# Checkout patterns
checkout_patterns = patterns('assets.views',
    url(r'^$', 'list', {'model': 'checkout'}, name='checkout_list'),
    url(r'^new/?', 'create_object', {'model': 'checkout'}, name='create_checkout'),
    url(r'^(?P<ID>[0-9]+)/?$', 'display_object', {'model': 'checkout'}, name='checkout'),
)

# Import urls
import_patterns = patterns('assets.views',
    url(r'^$', 'import_index', name='import'),
    url(r'^(?P<model>\w+)/?$', 'import_model', name='import_model'),
)

# Auth urls
auth_patterns = patterns('django.contrib.auth.views',
    url(r'^login/', 'login', {'template_name': 'login.html'}),
    url(r'^logout/', 'logout', {'next_page': '/'}),
)

# Tie it all together..
urlpatterns = patterns('',
    url(r'^$', 'assets.views.index', name='index'),
    url(r'^se', 'assets.views.ajax_search', name='ajax_search'),

    url(r'^asset/', include(asset_patterns)),
    url(r'^make/', include(make_patterns)),
    url(r'^model/', include(model_patterns)),
    url(r'^location/', include(location_patterns)),
    url(r'^checkout/', include(checkout_patterns)),

    url(r'^import/', include(import_patterns)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(auth_patterns)),
    url(r'^grappelli/', include('grappelli.urls')),
)
