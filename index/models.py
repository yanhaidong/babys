from django.db import models

# Create your models here.

class Blog_Model(models.Model):
    name = models.CharField(db_column='name', max_length=200, blank=True, verbose_name='name')
class Meta:
    db_table = 'Blog'
