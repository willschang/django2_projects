"""sensehiso_edu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 导入x admin，替换admin
import xadmin
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from rest_framework_swagger.views import get_swagger_view

from .api_urls import router
from .settings import MEDIA_ROOT

schema_view = get_swagger_view(title='Hiso EDU API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('api/v1/docs', schema_view),

    # api 接口 url
    re_path('^', include(router.urls)),
    # api 接口 url
    # re_path('api/', include('sensehiso_edu.api_urls')),
    # api docs
    path('api/docs/', include_docs_urls(title='SenseHiso EDU API DOCs')),
    # api 调试登录
    path('api-auth/', include('rest_framework.urls')),
    # drf 自带的token授权登录， 获取token需要向url post数据
    path('api-token-auth/', views.obtain_auth_token),

    # jwt token
    path('jwt-token', obtain_jwt_token),
    path('jwt-token-refresh/', refresh_jwt_token),

    path('', include('social_django.urls', namespace='social')),
    # TemplateView.as_view会将template转换为view
    path('', TemplateView.as_view(template_name="index.html"), name="index"),

    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    # re_path('static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),
    # 富文本相关url
    path('ueditor/', include('DjangoUeditor.urls')),

]
