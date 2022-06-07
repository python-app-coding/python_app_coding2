# coding：utf8
"""
标识编码格式需要符合下面正则表达式的匹配要求：
coding[=:]\s*([-\w.]+)

在文件的开始标识编码格式，可以使用下面的方式：
# -*- coding: utf8 -*-
# -*- coding = utf-8 -*-
# -*- encoding = utf8 -*-
# -*- coding = utf_8 -*-
# coding=utf8
# coding:utf8
"""

print("Hello, World！")
