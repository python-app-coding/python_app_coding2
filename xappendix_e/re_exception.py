# coding: utf8

"""
异常对象re.error带有下面的属性（Python 3.5之后增加）：
● msg：为格式化的异常信息。
● pattern：正则表达式。
● pos：编译失败的位置，有时可能为None。
● lineno：对应于pos的行号，有时可能为None。
● colno：对应于pos的列号，有时可能为None。
"""

import re

# 模式中存在错误：不允许*+的组合使用
z = "(\w+)*+"
# 编译时触发异常
# re.compile(z)
# Traceback (most recent call last):
# ......
# re.error: multiple repeat at position 6

# 捕获异常，并打印er属性信息
try:
    re.compile(z)
except re.error as er:
    print('msg:{}\npattern:{}\npos:{}\nlineno:{}\ncolno:{}'.
          format(er.msg,er.pattern, er.pos, er.lineno, er.colno))

# msg:multiplerepeat
# pattern:\w\w(?:\w+\.)*+
# pos:6
# lineno:1
# colno:7
