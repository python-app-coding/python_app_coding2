# coding = utf8

"""
◎ findall(string[, pos=0[, endpos=len(string)]])
搜索整个字符串，返回搜索结果为匹配内容的列表。
❑ string: 匹配字符串。
❑ pos: 可选参数。搜索字符串的起始位置，缺省为 0。
❑ endpos: 可选参数。搜索字符串的结束位置，缺省为字符串长度。
"""

import re

r = re.findall('([S|f]\S+)', 'the Song-123 is our favorite one!')
print(r)
# ['Song-123', 'favorite']
