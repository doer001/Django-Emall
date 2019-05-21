# Generated by Django 2.2.1 on 2019-05-13 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='昵称')),
                ('password', models.CharField(max_length=40, verbose_name='密码')),
                ('email', models.CharField(max_length=30, verbose_name='邮箱')),
                ('full_name', models.CharField(max_length=20, verbose_name='姓名')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('postcode', models.CharField(max_length=6, verbose_name='邮编')),
                ('phone', models.CharField(max_length=11, verbose_name='手机')),
            ],
        ),
    ]
