# coding: utf8

"""
fullmatch(pattern, string, flags=0)
匹配整个字符串，如果不匹配返回None。

"""

import re

# 可以匹配整个字符串
r = re.fullmatch('[A-Z]\w+ \w+ \w+', 'BBC animal video')
print(r)
# <re.Match object; span=(0, 16), match='BBC animal video'>

# 只能匹配部分字符串
print(re.fullmatch('[A-Z]\w+ \w+', 'BBC animal video'))
# None

# 对比match
r = re.match('[A-Z]\w+ \w+', 'BBC animal video')
print(r)
# <re.Match object; span=(0, 10), match='BBC animal'>
