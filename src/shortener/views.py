from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, get_object_or_404

from .models import ShortLink
from .serializers import ShortLinkSerializer


class CreateShortLinkAPIView(CreateAPIView):
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer


class RetrieveShortLinkAPIView(RetrieveAPIView):
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer
    lookup_url_kwarg = 'code'
    lookup_field = 'code'

    @method_decorator(cache_page(settings.SHORT_URL_CACHE_TIME))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ShortLinkRedirectView(RedirectView):

    def get_redirect_url(self, **kwargs):
        short_link = get_object_or_404(ShortLink, code=self.kwargs['code'])
        return short_link.url
