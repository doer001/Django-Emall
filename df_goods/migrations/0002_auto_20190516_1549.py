# Generated by Django 2.2.1 on 2019-05-16 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodsinfo',
            options={'verbose_name_plural': '商品'},
        ),
        migrations.AlterModelOptions(
            name='typeinfo',
            options={'verbose_name_plural': '商品分类'},
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='sale',
            field=models.IntegerField(default=0, verbose_name='商品销量'),
        ),
    ]