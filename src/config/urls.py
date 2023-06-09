from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .docs import schema_view

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='api_docs'),
    path('', include('shortener.urls')),
]

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
