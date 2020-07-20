from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from login import views

urlpatterns = [
    path("register/", obtain_jwt_token),
    path("captcha/", views.CaptchaAPIView.as_view()),
    path("enroll/", views.RegisterAPIViw.as_view()),
    path("verify/", views.VerifyAPIVew.as_view()),
    path("lone/", views.LoginMessageAPIView.as_view({"post": "login"})),
    path("mes/<str:mobile>", views.SendMessageAPIView.as_view()),
]
