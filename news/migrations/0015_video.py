# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-10 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_photo_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='视频名称')),
                ('path', models.CharField(max_length=256, verbose_name='视频路径')),
            ],
            options={
                'verbose_name': '图片路径',
                'verbose_name_plural': '图片路径',
            },
        ),
    ]
