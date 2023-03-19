from rest_framework import serializers
from rest_framework.reverse import reverse

from shortener.models import ShortLink


class LinkSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField('get_short_link')

    class Meta:
        model = ShortLink
        fields = ('url', 'short_url')

    def get_short_link(self, obj):
        return reverse('redirect_view', (obj.code,), request=self.context['request'])
