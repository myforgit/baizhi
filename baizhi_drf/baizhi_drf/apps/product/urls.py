from django.urls import path

from product import views

urlpatterns = [
    path("add_data/", views.Data.as_view({"post": "change_expire", "get": "get_select_course"})),
    path("add_cart/", views.Cart.as_view({"post": "add_product", "get": "List_product",
                                          "patch": "change_product", "put": "dele_produch", })),
]
