from django.urls import path

from course import views

urlpatterns = [
    path("course/", views.ListModel.as_view()),
    path("sum/", views.SumModel.as_view()),
    path("data/<str:id>", views.DataModel.as_view()),
    path("adp/", views.AdpModels.as_view()),
]
