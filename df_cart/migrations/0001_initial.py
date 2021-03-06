# Generated by Django 2.2.1 on 2019-05-16 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('df_goods', '0002_auto_20190516_1549'),
        ('df_user', '0002_auto_20190514_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='商品数量')),
                ('goods', models.ManyToManyField(to='df_goods.GoodsInfo', verbose_name='商品')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='df_user.UserInfo', verbose_name='所属用户')),
            ],
        ),
    ]
