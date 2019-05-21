from django.db import models
from df_goods.models import GoodsInfo
from df_user.models import UserInfo


# 主题是商品数量，该数同时绑定两个外键，即用户和商品
class Cart(models.Model):
    count = models.IntegerField(default=0, verbose_name='商品数量')
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='所属用户')
    goods = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, null=True, verbose_name='所属商品')

