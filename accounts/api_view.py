import datetime

from django.db.models import Q
# 因为自定义了 user， 用该函数 获得UserModel
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import list_route, detail_route, action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from .serializers import UserProfileSerializer, BannerSerializer
from .models import UserProfile, Banner
from .fitlers import BannerFilter

from common.api import APIResponse
from common.utils import CustomPaginationSerializer


User = get_user_model()

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
    viewsets demo  authentication
    """
    permission_classes = (IsAuthenticated, )
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    pagination_class = CustomPaginationSerializer

    # jwt验证权限
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    # 设置3大 常用过滤器，
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 排序设置
    ordering_fields = ('index',)
    # 设置 需要过滤的 字段
    # filter_fields = ('name', 'index')
    # 设置filter的类为 自定义的类
    filter_class = BannerFilter
    # 设置 search
    search_fields = ('title', 'index')


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

