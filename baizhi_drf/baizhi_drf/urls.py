"""baizhi_drf URL Configuration

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
import xadmin
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from xadmin.plugins import xversion

from django.conf import settings

xversion.register_models()

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path(r'media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("home/", include("home.urls")),
    path("login/", include("login.urls")),
    path("list/", include("course.urls")),
    path("add/", include("product.urls")),
    path("close/", include("order.urls")),
    path("payment/", include("payment.urls")),
]
