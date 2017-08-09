#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.db import models

class Article(models.Model):
    title = models.CharField('表题', max_length=40)
    desc = models.CharField('简介', max_length=200)
    content = models.TextField('内容')
    data_publish = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    link = models.CharField('链接', max_length=200)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title