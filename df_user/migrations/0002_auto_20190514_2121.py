# Generated by Django 2.2.1 on 2019-05-14 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='full_name',
            field=models.CharField(default='', max_length=20, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(default='', max_length=11, verbose_name='手机'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='postcode',
            field=models.CharField(default='', max_length=6, verbose_name='邮编'),
        ),
    ]
