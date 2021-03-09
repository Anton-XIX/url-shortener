from rest_framework import serializers
from .models import ShortLink


class ShortLinkListSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ShortLink
        fields = ['user', 'long_url', 'short_url', 'is_broken', 'last_validation']


class ShotlinkCreateSerializer(serializers.ModelSerializer):
    shorted_url = serializers.ReadOnlyField(source='short_url')

    class Meta:
        model = ShortLink
        fields = ['long_url', 'shorted_url']


class ShortLinkRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortLink
        fields = ['long_url', 'short_url']
