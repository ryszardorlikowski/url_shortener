from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers
from rest_framework.reverse import reverse

from shortener.models import ShortLink


class ShortLinkSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField('get_short_url')

    class Meta:
        model = ShortLink
        fields = ('code', 'url', 'short_url')
        read_only_fields = ('code',)

    def create(self, validated_data):
        instance, _ = ShortLink.objects.get_or_create(**validated_data)
        return instance

    @swagger_serializer_method(serializer_or_field=serializers.URLField)
    def get_short_url(self, obj):
        return reverse('redirect_view', (obj.code,), request=self.context['request'])
