# coding: utf8

"""
subn(pattern,repl,string,count=0,flags=0)
功能与re.sub一致，
返回结果为元组（new_string, number_of_subs_made），即替换后的字符串和替换的次数。
"""

import re

r = re.subn('([S|n]\S+)', 'song', 'Song-123 is nice!', count=3)
print(r)
# ('songis song', 2)