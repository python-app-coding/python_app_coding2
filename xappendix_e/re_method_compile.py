# coding: utf8

"""
compile(pattern[, flags])
编译生成Pattern对象，提供 match() 和 search() 函数使用。使用方式仍然等同原来的字符串描述模式，其作用是加快匹配的效率。
"""

import re

# 给定正则表达式
rs = "person"
# 编译正则表达式
cp = re.compile(rs)
# 使用编译的正则表达式进行匹配
r = re.match(cp,'person is a word.')
print(r)
# 'person'
