from django.db import models
from ckeditor.fields import RichTextField


class TypeInfo(models.Model):
    title = models.CharField(max_length=20, verbose_name='商品类名')
    isDelete = models.BooleanField(default=False, verbose_name='逻辑删除标志')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '商品分类'


class GoodsInfo(models.Model):
    title = models.CharField(max_length=20, verbose_name='商品名称')
    pic = models.ImageField(upload_to='df_goods', verbose_name='商品图片')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='商品价格')
    isDelete = models.BooleanField(default=False, verbose_name='逻辑删除标志')
    unit = models.CharField(max_length=20, verbose_name='商品单位')
    sale = models.IntegerField(verbose_name='商品销量', default=0)
    stock = models.IntegerField(verbose_name='商品库存')
    time = models.DateTimeField(auto_now_add=True, verbose_name='上架时间')
    description = models.CharField(max_length=200, verbose_name='商品描述')
    content = RichTextField(verbose_name='商品详情')

    type = models.ForeignKey(to=TypeInfo, on_delete=models.DO_NOTHING, verbose_name='所属类别')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '商品'



