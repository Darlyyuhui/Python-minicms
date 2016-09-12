# !/user/bin/python
# -*- coding: utf-8 -*-
'''
Created by zhangyh2 on 2016/9/12
@TODO:将对象内容转换为JSON格式，并进行字符串转换
数据进行转换的过程中，由于原始数据含有HTML标签，导致数据错误。
'''
import simplejson
from django.core.serializers import serialize
from django.db.models.query import QuerySet


def toJsonStr(obj):
    if isinstance(obj, QuerySet):
        print("isinstance   QuerySet")
        """ Queryset实例
        直接使用Django内置的序列化工具进行序列化
        但是如果直接返回serialize('json',obj)
        则在simplejson序列化时会被从当成字符串处理
        则会多出前后的双引号
        因此这里先获得序列化后的对象
        然后再用simplejson反序列化一次
        得到一个标准的字典（dict）对象
        """
        return strReplace(str(simplejson.loads(serialize('json', obj))))
    from django.db import models
    if isinstance(obj, models.Model):
        print("isinstance   Model")
        """
        如果传入的是单个对象，区别于QuerySet的就是
        Django不支持序列化单个对象
        因此，首先用单个对象来构造一个只有一个对象的数组
        这是就可以看做是QuerySet对象
        然后此时再用Django来进行序列化
        就如同处理QuerySet一样
        但是由于序列化QuerySet会被'[]'所包围
        因此使用string[1:-1]来去除
        由于序列化QuerySet而带入的'[]'
        """


        return strReplace(str(simplejson.loads(serialize('json', [obj])[1:-1])))
    if hasattr(obj, 'isoformat'):
        print("isinstance   处理日期类型")
    # 处理日期类型
        return strReplace(str(simplejson.JSONEncoder.default(obj)))

def strReplace(strs):
    s_quotes = str(strs).replace("\"", "\000")
    d_quotes = s_quotes.replace("\'", "\"")
    c_true = d_quotes.replace(": True", ": true")
    c_false = c_true.replace(": False", ": false")
    c_space = c_false.replace(" ", "\000")
    return  c_space