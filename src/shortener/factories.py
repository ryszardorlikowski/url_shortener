import factory

from .models import ShortLink


class ShortLinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShortLink
