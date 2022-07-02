# coding: utf8

"""
flags（正则表达式匹配标志）
该值为编译中设置的各种属性的组合值，即逻辑运算结果，如re.A|re.M。
包括模式内的分组内标志，如(?...)方式设置的分组内标志，以及隐含的标志，
如模式为Unicode字符串时的Unicode标志re.U。

>>> import re

# 缺省值为re.U
>>> rx = re.compile(u'[0-9]{3}')
>>> rx.flags
32

# 缺省值为re.A
>>> rx = re.compile(u'[0-9]{3}', re.A)
>>> rx.flags
256

groups（分组数）
模式中匹配分组的数目。没有分组时，值为0。
# 没有分组
>>> rx1 = re.compile('[0-9]')
>>> rx1.groups
0

# 有三个分组
>>> rx2 = re.compile(r'[,;|\ ]\s*(?P<g00>\.{0})()(?P<g01>\w+)')
>>> rx2.groups
3

groupindex（分组索引字典）
当模式中含有通过命名的分组时，该字典的元素为分组名称和组号的键值对，没有分组是空字典。
>>> rx2.groupindex
mappingproxy({'g00': 1, 'g01': 3})

pattern（模式源串）
用于编译的匹配模式源字符串。
>>> rx1.pattern
'[0-9]'
"""
