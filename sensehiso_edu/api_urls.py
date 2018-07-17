from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from .routers import router


urlpatterns = [
    path('accounts/', include('accounts.api_urls')),

]

urlpatterns += [
    path('', include(router.urls)),
]
