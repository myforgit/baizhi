import xadmin
from .models import Order
from .models import OrderDetail


class OrderModel(object):
    """商品活动模型"""
    pass


xadmin.site.register(Order, OrderModel)


class OrderDetailModel(object):
    """课程有效期模型"""
    pass


xadmin.site.register(OrderDetail, OrderDetailModel)
