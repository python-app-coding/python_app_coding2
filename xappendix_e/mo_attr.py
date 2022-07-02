# coding: utf8

"""
● pos（匹配开始位置）
传递给正则表达式对象方法match()和search()的匹配开始位置值，在该下标处模式开始进行匹配。

>>> import re


【示例】
>>> mo1 = re.search('([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})','ip:1.102.3.168')
>>> mo1.pos
0

● endpos（匹配停止位置）
传递给正则表达式对象的match()和search()方法的匹配结束位置值，在该下标处模式停止进行匹配。

【示例】
>>> mo1.endpos
14

● lastindex
最后匹配分组的索引值，如果没有分组匹配则为None。
例如，当模式‘(a)b’、‘((a)(b))’、‘((ab))’用于匹配‘ab’时，lastindex为1，而使用模式‘(a)(b)’匹配‘ab’时，lastindex的值为2。

【示例】
只有一个分组：
>>> mo2 = re.search('(a)b','ab')
>>> mo2.lastindex
1

存在两个分组：
>>> mo3 = re.search('(a)(b)','ab')
>>> mo3.lastindex
2

存在三个分组，空匹配仍然计算在内：
# 有三个分组
>>> mo4 = re.search('(a)(b)([0-9]*)', 'ab')
>>> mo4.groups()
('a', 'b', '')
>>> mo4.lastindex
3

没有分组，lastindex为None：
>>> mo5 = re.search('ab','abc')
>>> mo5.group(0), mo5.groups()
('ab', ())
>>> mo5.lastindex is None
True

● lastgroup
最后匹配成功的分组的名称，如果没有分组名称或没有分组匹配则返回None。

【示例】
# 返回最后匹配的分组名
>>> mo6 = re.search('(a)(b)(?P<empty_group>[0-9]*)','ab')
>>> mo6.lastgroup
'empty_group'

# 最后匹配的分组没有名称，lastgroup为None
>>> mo7 = re.search('(?P<first_group>a)(b)([0-9]*)','ab')
>>> mo7.lastgroup is None
True

# 判断匹配是否成功
>>> mo8 = re.search('[a-z]{2}','ab')
>>> mo8 is None
False

● re
用于该匹配对象的正则表达式对象，方法match()或search()使用该模式进行匹配。

【示例】
>>> mo9 = re.match('[0-9]{3}\w{2}', '123ab-ed')
>>> mo9.re
re.compile(r'[0-9]{3}\\w{2}')

● string
传递给方法match()或search()进行匹配的字符串。

【示例】
>>> mo10 = re.match('[ab]{2}\w{1}', 'abcab')
>>> mo10.string
'abcab'
"""