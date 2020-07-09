from rest_framework import serializers

from home.models import Banner


class BannerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ("img", 'link')
