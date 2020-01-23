from django.db import models


class GoodsType(models.Model):
    type_name = models.CharField(max_length=32)
    type_pic = models.ImageField(upload_to='store_static/img')


class Goods(models.Model):
    name = models.CharField(max_length=128)
    store = models.CharField(max_length=128)
    price = models.FloatField()
    safe_date = models.DateField()
    picture = models.ImageField(upload_to='store_static/img')
    number = models.IntegerField()
    description = models.TextField()
    status = models.IntegerField(default=1)  # 1为 上架  0 为下架
    goods_type = models.ForeignKey(to=GoodsType, on_delete=models.CASCADE, default=1)
