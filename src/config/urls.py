from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .docs import schema_view

# Prefix to be used on all v1 API urls
v1_prefix = 'v1/'


def v1_url(url):
    # Prepend a url string with the v1 prefix.
    return v1_prefix + url


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path(v1_url('docs/'), schema_view.with_ui('redoc', cache_timeout=0), name='api_docs'),
]

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
