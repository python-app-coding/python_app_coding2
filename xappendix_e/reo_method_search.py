# coding: utf8

"""
search(string[,pos[,endpos]])
搜索字符串string，找到第一个子串与模式匹配成功，则返回相应的匹配对象，未搜到匹配子串则返回None。
但是，返回None与0的情况并不相同，有些带有'*'或'?'控制符的匹配，可以返回0长度匹配，但不是None。
pos和exnpos是可选参数，指定匹配搜索的开始和结束位置。
pos缺省值是0，endpos的缺省值是字符串的长度。如果endpos的值小于pos，则匹配结果是None。
pos的使用不完全等同于对字符串进行切片，匹配符'^'匹配字符串的开始位置，
在一个新行开始之后，不一定是匹配搜索开始的位置。

>>> import re

# 【编译生成REO示例】
>>> ps1 ='[A-Z]-[0-9]{2}'		# 正则表达式
>>> rx = re.compile(ps1)		# 编译生成REO

>>> rx.search('A-01,B-02')      # 匹配成功'A-01'
<re.Match object; span=(0, 4), match='A-01'>

# 【设置位置参数pos、endpos示例】
>>> rx.search('A-01,B-02,c-03',pos=3, endpos=10)	# 从位置2开始搜索，匹配成功'B-02'
<re.Match object; span=(5, 9), match='B-02'>

>>> rx.search('A-01,B-02,c-03'[3:10])	# 等同于pos=3, endpos=10
<re.Match object; span=(2, 6), match='B-02'>

# 【空匹配返回空字符串】
>>> ps2 ='\d*'
>>> rx = re.compile(ps2)
>>> rx.search('abc')    # 返回零长度匹配，但不是None
<re.Match object; span=(0, 0), match=''>
"""


