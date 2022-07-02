# coding: utf8

"""
常用正则表达式

>>> import re

◎ 匹配数字、字母或下划线组成非空字符串。如，'bj212'，'10'，'Win'。
【模式】
'[0-9a-zA-Z\_]+'
【示例】
>>> re.findall('(bj[0-9]{3})', 'bj212, new bj212, bj212a!')
['bj212', 'bj212', 'bj212']

◎ 匹配以abc开始的字符串。如，^abc匹配以abc开始的字符串。
【模式】
'^xxx'
【示例】
>>> re.match('^dis\w+', 'discovery animal video')
<re.Match object; span=(0, 9), match='discovery'>

◎ 匹配不在[]中的字符。如，[^abc] 匹配除了a,b,c之外的字符。
【模式】
'[^xxx]'
【示例】
>>> re.match('[^abc]\w+', 'discovery animal video')
<re.Match object; span=(0, 9), match='discovery'>

◎ 结尾单词匹配。如，abc$匹配以abc结尾的字符串
【模式】
'xxx$'
【示例】
>>> re.match('(^dis)\w+.?\w+(al$)', 'discovery-animal')
<re.Match object; span=(0, 16), match='discovery-animal'>

◎ 匹配可选择字符。如，(P|p)ython匹配'Python'或'Python'。
【模式】
'x|y'
【示例】
>>> re.match('(P|p)ython','python language')
<re.Match object; span=(0, 6), match='python'>

◎ 以数字开头的模式。
【模式】
'^\d'
【示例】
>>> re.match('^\d[a-z]{4}','3miles')
<re.Match object; span=(0, 5), match='3mile'>

◎ 特定大小写组合匹配。如‘[A|a]b[c|D]’可匹配Abc、abc、AbD、abD。
【模式】
'[X|x...]'
【示例】
>>> re.findall('[c|C]o[D|d]e', 'Ok, code Code COde CoDe')
['code', 'Code', 'CoDe']

◎ 特定词组检测。如‘We|He|this’可匹配单词We、He、this之一。
【模式】
'[xxx|yyy|...]'
【示例】
>>> re.findall('cn|us|uk', 'cn is for china, us is for America, uk for Englis')
['cn', 'us', 'uk']

◎ 匹配长度m至n的数字字母下划线字符串。
【模式】
'[0-9a-zA-Z]{m,n}'
【示例】
>>> re.findall('[0-9a-zA-Z\_]{2,3}', '1 12 123 1234 12345')
['12', '123', '123', '123', '45']

◎ 匹配长度为m-n的数字字符串。
【模式】
'\d{m,n}'
【示例】
>>> re.findall('\d{1,4}','aaa1234bbb12345ccc123456')
['1234', '1234', '5', '1234', '56']

◎ 匹配ASCII码串。
【模式】
'[\u0001-\u00FF]+'
【示例】
>>> s='code代码and编程program'
>>> regex='[\u0001-\u00FF]+'
>>> re.findall(regex, s)# 返回结果：['code','and','program']
['code', 'and', 'program']

# ◎ 匹配中文字符。
# Unicode基本汉字编码范围为U+4e00-U+9fa5，故用“[\u4e00-\u9fa5]+”检测常用中文字符。
# 同时，由于Unicode中文字符集进行了多次扩充，分散于多个编码区，如进行严格的匹配，需要注意分区范围。
# 匹配所有汉字需使用'\\U000XXXXX'格式的编码，如扩展B区的编码匹配表达式为 [\\U00020000-\\U0002A6D6]。
#
# 【模式】
# '[\u4e00-\u9fa5]+'
# 【示例】
>>> s='super超级程序员super-programmer超级程序xprogram'
>>> re.findall('[\u4e00-\u9fa5]+', s)
['超级程序员', '超级程序']

>>> re.match('[\U00020000-\U0002a6d6]', '\U00020001')   # 有些环境不支持扩展编码，结果可能会显示为空格
<re.Match object; span=(0, 1), match='𠀁'>
"""
