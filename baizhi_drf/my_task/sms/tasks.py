import logging

from baizhi_drf.settings import constants
from baizhi_drf.util.send_msg import Message
from my_task.main import app

logger = logging.getLogger('django')


@app.task(name="send_sms")
def send_sms(mobile, code):
    print("这是发送短信的方法")
    message = Message(constants.API_KEY)
    status = message.send_message(mobile, code)
    if status:
        logger.error("用户发送短信失败，手机号为：%s" % mobile)
    return "hello"


@app.task(name="check_order")
def check_order():
    """完成过期取消订单"""
    print("根据时间点判断订单支付时间是否超时")
