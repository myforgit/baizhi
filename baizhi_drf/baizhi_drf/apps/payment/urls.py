from django.urls import path

from payment import views

urlpatterns = [
    path("money/", views.PaymentModel.as_view()),
    path("money_apy/", views.AliPaymentAPIView.as_view()),
]