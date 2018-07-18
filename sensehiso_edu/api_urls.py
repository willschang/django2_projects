# from django.urls import include, path, re_path
# from rest_framework.routers import DefaultRouter
# from .routers import router
#
#
# urlpatterns = [
#     path('accounts/', include('accounts.api_urls')),
#
# ]
#
# urlpatterns += [
#     path('', include(router.urls)),
# ]

from .routers import router

from accounts.api_view import BannerGenericViewSet, BannerGenericViewSet1

router.register(r'demo', BannerGenericViewSet)
router.register(r'demo_test', BannerGenericViewSet1)