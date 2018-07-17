from .serializers import UserProfileSerializer, BannerSerializer
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import list_route, detail_route, action
from common.api import APIResponse

from .models import UserProfile, Banner

from common.utils import CustomPaginationSerializer


class BannerViewSet(APIView):
    def get(self, request):
        banner = Banner.objects.all()
        data = BannerSerializer(banner, many=True)
        return APIResponse(data.data)


# class BannerListViewSet(mixins.ListModelMixin, generics.GenericAPIView):
class BannerListViewSet(generics.ListAPIView):
    """

    """
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    pagination_class = CustomPaginationSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)


class BannerGenericViewSet(GenericViewSet):
    """
    viewsets demo
    """
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    pagination_class = CustomPaginationSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        data = BannerSerializer(self.queryset, many=True).data
        return APIResponse(data)


    @action(methods=['get'], detail=False)
    def demo_action(self, request, *args, **kwargs):
        """
        action 装饰器
        自定义 分页功能

        """
        page = self.paginate_queryset(self.queryset)
        data = BannerSerializer(page, many=True).data
        return self.get_paginated_response(data)


class BannerGenericViewSet1(GenericViewSet):
    """
    viewsets demo
    """
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    pagination_class = CustomPaginationSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        data = BannerSerializer(self.queryset, many=True).data
        return APIResponse(data)


    @action(methods=['get'], detail=False)
    def demo_action1(self, request, *args, **kwargs):
        """
        action 装饰器
        自定义 分页功能

        """
        data = BannerSerializer(self.queryset, many=True).data
        return APIResponse(data)

