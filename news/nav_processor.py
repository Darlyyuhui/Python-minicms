# !/user/bin/python
# -*- coding: utf-8 -*-
'''
Created by zhangyh2 on 2016/9/7
@TODO:
'''

from .models import Column

nav_display_columns = Column.objects.filter(nav_display=True)

def nav_column(request):
    return {'nav_display_columns': nav_display_columns}