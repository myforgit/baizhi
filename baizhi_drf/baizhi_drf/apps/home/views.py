from rest_framework.generics import ListAPIView

from home.models import Banner
from home.serializers import BannerModelSerializer


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by("-orders")
    serializer_class = BannerModelSerializer
