from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import OrderingFilter

from course.models import Course, CourseCategory, CourseChapter
from course.pagination import CoursePageNumber
from course.seriallzer import CourseModelSerializer, CourseCategorySerializer, DataModelSerializer, AdpModel


class SumModel(ListAPIView):
    """#课程分类"""
    queryset = CourseCategory.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseCategorySerializer


class ListModel(ListAPIView):
    """#课程详细分类"""
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseModelSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ("course_category",)
    # 排序
    ordering_fields = ("id", "students", "price")
    # 分页   只能有一个
    pagination_class = CoursePageNumber


class DataModel(RetrieveAPIView):
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = DataModelSerializer
    lookup_field = 'id'


class AdpModels(ListAPIView):
    queryset = CourseChapter.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = AdpModel
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["course"]
