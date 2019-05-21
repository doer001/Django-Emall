from django.db import models


class Order(models.Model):
    user = models.ForeignKey('df_user.UserInfo', on_delete=models.CASCADE, verbose_name='收货人')
    address = models.CharField(max_length=100, verbose_name='收货人地址')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='提交订单时间')
    is_paid = models.BooleanField(default=False, verbose_name='是否已付钱')
    total = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='总价')

    def __str__(self):
        return '{}在{}提交的订单'.format(self.user.username, self.datetime)

    class Meta:
        verbose_name = verbose_name_plural = '订单'


class OrderDetail(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='商品价格')
    count = models.IntegerField(verbose_name='商品数量')
    goods = models.ForeignKey('df_goods.GoodsInfo', on_delete=models.CASCADE, verbose_name='商品')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='订单')

    def __str__(self):
        # return self.goods.title + "(数量为" + str(self.count)  + ")"
        return "{0}(数量为{1})".format(self.goods.title, self.count)

    class Meta:
        verbose_name = verbose_name_plural = '订单详情'
