# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-07 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20160907_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(db_index=True, max_length=256, verbose_name='网址'),
        ),
    ]
