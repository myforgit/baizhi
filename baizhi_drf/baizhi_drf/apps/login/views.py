import random
import re

from django_filters.rest_framework import DjangoFilterBackend
from django_redis import get_redis_connection
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status as http_status, serializers, status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.viewsets import ViewSet

from baizhi_drf.libs.geetest import GeetestLib
from baizhi_drf.settings import constants

from login.models import UserInfo
from login.serializers import UserModelSerializer, LoginModel
from login.utils import get_user_by_account
from utils.random_code import get_random_code
from utils.send_msg import Message

pc_geetest_id = "6f91b3d2afe94ed29da03c14988fb4ef"
pc_geetest_key = "7a01b1933685931ef5eaf5dabefd3df2"


# 验证码登录逻辑
class CaptchaAPIView(APIView):
    """极验验证码"""

    user_id = 0
    status = False

    def get(self, request, *args, **kwargs):
        """获取验证码"""

        username = request.query_params.get('username')
        user = get_user_by_account(username)
        if user is None:
            return Response({"message": "用户不存在"}, status=http_status.HTTP_400_BAD_REQUEST)

        self.user_id = user.id

        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        self.status = gt.pre_process(self.user_id)
        response_str = gt.get_response_str()
        return Response(response_str)

    def post(self, request, *args, **kwargs):
        """验证验证码"""
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        # 判断用户是否存在
        if self.user_id:
            result = gt.success_validate(challenge, validate, seccode, self.user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        result = {"status": "success"} if result else {"status": "fail"}
        return Response(result)


# 注册逻辑
class RegisterAPIViw(CreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserModelSerializer


# 用户输入手机号后进行验证
class VerifyAPIVew(APIView):
    def post(self, request, *args, **kwargs):
        phone = request.data.get("phone")
        if not re.match(r'^1[3-9]\d{9}$', phone):
            return Response({"message": "手机格式不正确"}, status=http_status.HTTP_404_NOT_FOUND)

        user_phone = UserInfo.objects.filter(phone=phone)

        if user_phone:
            return Response({"message": "该手机号已经被注册"}, status=http_status.HTTP_400_BAD_REQUEST)

        return Response({"message": "OK"})


# 短信发送
class SendMessageAPIView(APIView):

    def get(self, request, mobile):
        """
        获取验证码  为手机号生成验证码并发送
        :param request:
        :param mobile: 手机号
        :return:
        """
        # 获取redis连接
        redis_connection = get_redis_connection("sms_code")

        # TODO 1. 判断手机验证码是否在60s内发送过短信
        mobile_code = redis_connection.get("sms_%s" % mobile)
        if mobile_code is not None:
            return Response({"message": "您已经在60s内发送过短息了~"}, status=http_status.HTTP_400_BAD_REQUEST)

        # 2. 生成随机的短信验证码
        code = "%06d" % random.randint(0, 999999)

        # 3. 将验证码保存到redis中
        redis_connection.setex("sms_%s" % mobile, constants.SMS_EXPIRE_TIME, code)  # 60s不允许再发送
        redis_connection.setex("mobile_%s" % mobile, constants.MOBILE_EXPIRE_TIME, code)  # 验证码的有效时间

        # 4. 调用方法  完成短信的发送
        try:
            from my_task.sms.tasks import send_sms
            send_sms.delay(mobile, code)
        except:
            return Response({"message": "短信发送失败"}, status=http_status.HTTP_500_INTERNAL_SERVER_ERROR)

        # 5. 响应回去
        return Response({"message": "发送短信成功"}, status=http_status.HTTP_200_OK)


class LoginMessageAPIView(ViewSet):

    def login(self, request, *args, **kwargs):
        phone = request.data.get("phone")
        try:
            phone_ser = UserInfo.objects.get(phone=phone)
        except:
            return Response({"message": "该用户不存在"})
        book_obj = LoginModel(phone_ser).data
        from rest_framework_jwt.settings import api_settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(phone_ser)
        token = jwt_encode_handler(payload)
        return Response({
            "status": status.HTTP_200_OK,
            "mig": "查询单个用户成功！",
            "request": book_obj,
            "token": token,
        })
