from rest_framework import serializers

from course.models import Course, Teacher, CourseCategory, CourseChapter, CourseLesson


class CourseCategorySerializer(serializers.ModelSerializer):
    """课程分类"""

    class Meta:
        model = CourseCategory
        fields = ["id", "name"]


class CourseTeacherSerializer(serializers.ModelSerializer):
    """课程所属老师的序列化器"""

    class Meta:
        model = Teacher
        fields = ("id", "name", "title", "signature", "brief", "image")


class CourseModelSerializer(serializers.ModelSerializer):
    """课程列表"""

    # 序列化器嵌套查询老师信息
    teacher = CourseTeacherSerializer()

    class Meta:
        model = Course
        fields = ["id", "name", "course_img", "students", "lessons",
                  "pub_lessons", "price", "teacher", "lesson_list", "nuw_name", "nuw_price"]


class DataModelSerializer(serializers.ModelSerializer):
    teacher = CourseTeacherSerializer()

    class Meta:
        model = Course
        fields = ["id", "name", "course_img", "students", "lessons",
                  "pub_lessons", "price", "teacher", "level_name",
                  "brief_html", "course_category", "course_video", "nuw_name", "nuw_price", "count_down"]


# 购物车
class LessonModel(serializers.ModelSerializer):
    class Meta:
        model = CourseLesson
        fields = ("id", "name", "free_trail")


class AdpModel(serializers.ModelSerializer):
    coursesections = LessonModel(many=True)

    class Meta:
        model = CourseChapter
        fields = ("id", "chapter", "name", "coursesections", "course")
