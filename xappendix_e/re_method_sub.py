# coding: utf8

"""
◎ sub(pattern, repl,dest, count=0, flags=0)
查找符合模式的子串，并使用repl替换匹配子串，返回替换后的字符串。
❑ pattern : 模式字符串。
❑ repl :用于替换的字符串。
❑ dest: 被查找替换的字符串。
❑ count : 匹配替换的最大次数，缺省值为0，表示替换所有匹配。
注： 1）3.1版后，sub增加了flags标志参数；
    2）3.5版后，未匹配的组使用空串替换；
    3）3.6版后，模式中未定义的转义符（\与ASCII字母的组合）视为错误；4）3.7版后，在替换字符串repl中,
      未定义的转义符（\与ASCII字母的组合）视为错误,空匹配使用前一个邻接的非空匹配代替。
"""

import re


r = re.sub('([S|f]\S+)','song', 'The Song-123 is our favorite one!')
print(r)
# 'Thesong is our song one!'

# 设置count，限制匹配次数
r = re.sub('([S|f]\S+)','song', 'The Song-123 is our favorite one!', count=1)
print(r)
# 'Thesong is our favorite one!'

r = re.sub('([a-z]{4})', '***', 'Song-123 is nice!', count=3)
print(r)
# 'Song-123is ***!'

# 未匹配使用空串替换，没有改变原字符串
r = re.sub('([a-z]{6})', '***', 'Song-123 is nice!', count=3)
print(r)
# 'Song-123is nice!'

# 使用未定义转义组合，产生语法错误！
# r = re.sub('\x{4}', '***', 'Song-123 is nice!', count=3)
# File"<ipython-input-93-619aa7edbe8d>", line 1
# re.sub('\x{4}','***', 'Song-123 is nice!', count=3)
# ^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-1: truncated \xXX escape