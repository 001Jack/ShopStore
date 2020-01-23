from django.db import models


# Create your models here.

# 用户表
class User(models.Model):
    username = models.CharField(max_length=32)  # 用户名
    password = models.CharField(max_length=32)  # 密码
    email = models.EmailField()  # 用户邮箱


# 用户详情
class QuserInfo(models.Model):
    phone = models.CharField(max_length=32)
    address = models.TextField()
    photo = models.ImageField(upload_to="user/img", default="user/img/photo.jpg")
    has_store = models.IntegerField()  # 0 否   1 是
    user_id = models.OneToOneField(to=User, on_delete=models.CASCADE)


# 用户地址
class Address(models.Model):
    recipients = models.CharField(max_length=32)  # 收件人
    address = models.TextField()
    postcode = models.CharField(max_length=32)  # 邮编
    phone = models.CharField(max_length=32)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    is_now = models.IntegerField(default=0)  # 0默认地址 1当前地址


# 购物车
class BuyCar(models.Model):
    goods_name = models.CharField(max_length=32)
    goods_price = models.FloatField()
    goods_number = models.IntegerField()  # 购买数量   1<= 购买数量 <= 进货数量
    goods_picture = models.CharField(max_length=32)
    goods_store = models.IntegerField()  # 店铺id
    goods_total = models.FloatField()  # 总价各
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)


class PayOrder(models.Model):
    pay_number = models.CharField(max_length=32)
    pay_price = models.FloatField(default=0)  # 订单总计
    pay_status = models.IntegerField()  # 1未支付  2支付未发货   3、待收货   4确认收货
    goods_total = models.IntegerField()  # 商品总数量
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    address = models.ForeignKey(to=Address, on_delete=models.CASCADE)


class PayInfo(models.Model):
    goods_name = models.CharField(max_length=32)
    goods_price = models.FloatField()
    goods_number = models.IntegerField()  # 购买数量   1<= 购买数量 <= 进货数量
    goods_total = models.FloatField()  # 商品小计
    goods_picture = models.CharField(max_length=32)
    goods_store = models.IntegerField()  # 店铺id
    pay_status = models.IntegerField()  # 1未支付  2支付未发货   3、待收货   4确认收货   5(退货)
    order_id = models.ForeignKey(to=PayOrder, on_delete=models.CASCADE)


class Cpassword(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=32)
    is_chage = models.IntegerField()
