# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import time
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField


@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField(u'栏目名称',max_length=256)
    slug = models.CharField(u'栏目网址',max_length=256,db_index=True)
    intro = models.TextField(u'栏目简介',default='')

    #添加导航
    nav_display = models.BooleanField(u'导航显示',default=False)
    home_display = models.BooleanField(u'首页显示',default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('column',args=(self.slug,))

    class Meta:
        verbose_name = '新闻分组'
        verbose_name_plural = '新闻分组'
        ordering = ['name'] #按照哪个栏目排序

@python_2_unicode_compatible
class Photo(models.Model):
    name = models.CharField(u'图片名称', max_length=256)
    image = models.FileField(u'图片', upload_to='Images', max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '图片路径'
        verbose_name_plural = '图片路径'

@python_2_unicode_compatible
class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name = '归属栏目')
    photo = models.ManyToManyField(Photo,verbose_name = '图片')
    title = models.CharField(u'标题',max_length=256)
    slug = models.CharField(u'网址',max_length=256)

    author = models.ForeignKey('auth.User',blank=True,null=True,verbose_name='作者')
    keyword = models.CharField(u'关键字', max_length=256,default='')
    content = UEditorField(u'内容',height=300,width=1000,
                           default=u'',blank=True,imagePath="uploads/images/",
                           toolbars='besttome',filePath='uploads/files/')
        #models.TextField(u'内容',default='',blank=True)
    image = models.FileField(u'图片路径',upload_to='Images', max_length=100)
    published = models.BooleanField(u'正式发布',default=True)

    pub_date = models.DateTimeField(u'发表时间',auto_now_add=True,editable=True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True,null=True)


    def __str__(self):
        return  self.title

    def get_absolute_url(self):
        return reverse('article',args=(self.pk,self.slug,))

    def getPub_date(self):
        return time.strftime("%Y-%m-%d %H:%M:%S",time.mktime(self.pub_date))

    class Meta:
        verbose_name = '新闻文章'
        verbose_name_plural = '新闻文章'

@python_2_unicode_compatible
class Video(models.Model):
    name = models.CharField(u'视频名称', max_length=256)
    path = models.CharField(u'视频路径', max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('video',args=(self.pk,))


    class Meta:
        verbose_name = '视频集合'
        verbose_name_plural = '视频集合'




