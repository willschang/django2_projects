from django.urls import path
from django.conf.urls import url, include
from .api_view import BannerViewSet, BannerListViewSet, BannerGenericViewSet
from sensehiso_edu.routers import router


router.register(r'demo', BannerGenericViewSet)

urlpatterns = [
    path('banners1/', BannerViewSet.as_view()),
    path('demo1/', BannerListViewSet.as_view()),
]


urlpatterns += [
    path('', include(router.urls))
]
