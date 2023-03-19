from django.views.generic import RedirectView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, get_object_or_404

from .models import ShortLink
from .serializers import LinkSerializer


class CreateShortLinkAPIView(CreateAPIView):
    queryset = ShortLink.objects.all()
    serializer_class = LinkSerializer


class RetrieveShortLinkAPIView(RetrieveAPIView):
    queryset = ShortLink.objects.all()
    serializer_class = LinkSerializer
    lookup_url_kwarg = 'code'
    lookup_field = 'code'


class ShortLinkRedirectView(RedirectView):

    def get_redirect_url(self, **kwargs):
        short_link = get_object_or_404(ShortLink, code=self.kwargs['code'])
        return short_link.url
