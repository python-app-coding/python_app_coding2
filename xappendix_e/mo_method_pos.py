# coding: utf8

"""
◎ start([group])
◎ end([group])
返回分组匹配中子串的开始、结束位置。返回值为0时，指匹配了整个字符串，返回值为-1时，指存在分组但未匹配。
对于一个匹配对象m和一个匹配分组g，匹配子串m.group(g)可以表示为原串的位置切片。二者是相等的。
如果分组g匹配了空串，m.start(g)和m.end(g)是相等的。
如果分组名称或编号不存在，在m.start和m.end()中引用则会引发IndexError异常。

>>> import re

【示例】
>>> mo19 = re.match('(?P<first_name>[0-9]{3})(\s*)(\w+)', '123ab')
>>> mo19.groups()
('123', '', 'ab')

# 原字符串位置切片与group参数引用等同
>>> g ='first_name'
>>> mo19.string[mo19.start(g):mo19.end(g)]== mo19.group(g)
True

# 空匹配的分组，起始位置等于结束位置
>>> mo19.start(2), mo19.end(2)
(3, 3)
"""