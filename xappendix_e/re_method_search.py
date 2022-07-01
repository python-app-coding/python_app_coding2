# coding = utf8
"""
使用模式字符串pattern，搜索整个字符串string，
匹配成功返回匹配对象，否则返回None。
类似match，可以使用groups()来获取匹配表达式。
"""
import re


r = re.search(r'(\b[a-eB]{3}\b)','Hume and Bea young')

print(r)
# <re.Match object; span=(9, 12), match='Bea'>

print(r.groups())
# ('Bea',)

print(r.group(0))
# Bea
