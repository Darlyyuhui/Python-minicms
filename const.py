# !/user/bin/python
# -*- coding: utf-8 -*-
'''
Created by zhangyh2 on 2016/9/8
@TODO:常量类
'''
class _const:
    class ConstError(TypeError):
        pass
    def __setattr__(self, key, value):
        if self.__dict__.has_key(key):
            raise self.ConstError; "Can't rebind const (%s)" %key
        self.__dict__[key] = value

import sys
sys.modules[__name__]= _const
_const.magic = 23
_const.magic = 33
