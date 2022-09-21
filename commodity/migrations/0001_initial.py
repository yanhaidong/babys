# Generated by Django 4.0.6 on 2022-08-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommodityInfos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='商品名称')),
                ('sezes', models.CharField(max_length=100, verbose_name='商品规格')),
                ('types', models.CharField(max_length=100, verbose_name='商品类型')),
                ('price', models.FloatField(verbose_name='商品价格')),
                ('discount', models.FloatField(verbose_name='折扣价格')),
                ('stock', models.IntegerField(verbose_name='存货数量')),
                ('sold', models.IntegerField(verbose_name='已售数量')),
                ('likes', models.IntegerField(verbose_name='收藏数量')),
                ('created', models.DateField(auto_now_add=True, verbose_name='上架日期')),
                ('img', models.FileField(upload_to='img', verbose_name='商品图片')),
                ('details', models.FileField(upload_to='details', verbose_name='商品介绍')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firsts', models.CharField(max_length=100, verbose_name='一级类型')),
                ('second', models.CharField(max_length=100, verbose_name='二级类型')),
            ],
            options={
                'verbose_name': '商品类型',
                'verbose_name_plural': '商品类型',
            },
        ),
    ]
