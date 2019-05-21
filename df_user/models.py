from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=20, verbose_name='昵称')
    password = models.CharField(max_length=40, verbose_name='密码')
    email = models.CharField(max_length=30, verbose_name='邮箱')
    full_name = models.CharField(max_length=20, default='', verbose_name='姓名')
    address = models.CharField(max_length=100, default='', verbose_name='地址')
    postcode = models.CharField(max_length=6, default='', verbose_name='邮编')
    phone = models.CharField(max_length=11, default='', verbose_name='手机')
    # default, blank 是 python 层面的约束，不影响表结构

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = '用户'
        verbose_name = '用户'
