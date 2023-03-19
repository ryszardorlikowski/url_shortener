from django.urls import path

from .views import CreateShortLinkAPIView, RetrieveShortLinkAPIView, ShortLinkRedirectView

urlpatterns = [
    path('short-links', CreateShortLinkAPIView.as_view(), name='create_short_link'),
    path('short-links/<str:code>', RetrieveShortLinkAPIView.as_view(), name='get_short_link'),
    path('<str:code>', ShortLinkRedirectView.as_view(), name='redirect_view'),
]
