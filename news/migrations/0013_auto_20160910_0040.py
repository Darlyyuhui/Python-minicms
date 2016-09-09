# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-09 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20160909_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='Images', verbose_name='图片')),
            ],
            options={
                'verbose_name': '图片路径',
                'verbose_name_plural': '图片路径',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ManyToManyField(to='news.Photo', verbose_name='图片'),
        ),
    ]
