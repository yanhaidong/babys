from django.db import models

# Create your models here.
class Types(models.Model):
    id = models.AutoField(primary_key=True)#主键
    firsts = models.CharField('一级类型',max_length=100)
    second = models.CharField('二级类型',max_length=100)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '商品类型'
        verbose_name_plural = '商品类型'

class CommodityInfos(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField('商品名称',max_length=100)
    sezes = models.CharField('商品规格',max_length=100)
    types = models.CharField('商品类型',max_length=100)
    price = models.FloatField('商品价格')
    discount = models.FloatField('折扣价格')
    stock = models.IntegerField('存货数量')
    sold = models.IntegerField('已售数量')
    likes = models.IntegerField('收藏数量')
    created=models.DateField('上架日期',auto_now_add=True)
    #FileField  upload_to 用于保存上传文件的本地文件系统路径，该路径由 MEDIA_ROOT 中设置
    img = models.FileField('商品图片',upload_to='img')
    details = models.FileField('商品介绍',upload_to='details')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'

