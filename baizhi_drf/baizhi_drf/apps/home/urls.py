from django.urls import path

from home import views

urlpatterns = [
    path("banner/", views.BannerListAPIView.as_view()),
    path("hed/", views.HomeListAPIView.as_view()),
    path("fle/", views.FleListAPIView.as_view()),
]
