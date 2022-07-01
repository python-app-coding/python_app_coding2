# coding: utf8

"""
match(string[,pos[,endpos]])
从字符串开始匹配模式，如果成功返回匹配对象，否则返回None。其pos和endpos的使用方式与search方法相同。

>>> import re

【使用REO进行匹配示例】
# 编译正则表达式生成REO 
>>> ps1 ='[0-9]{4}-[0-9]{8}'
>>> rx1 = re.compile(ps1)

# 使用REO进行匹配，检测是否匹配成功
>>> rx1.match('0531-81298111') is None
False

【使用flags参数示例】
>>> ps2 ='\w{3}'
>>> rx2 = re.compile(ps2)
>>> rx2.match('\u0660ab') is None	# 检验\w是否可以匹配非ASCII字符,	匹功非ASCII码字符成功
False

>>> rx3 = re.compile(ps2, flags=re.A)	    # 设置标志仅对ASCII码进行匹配
>>> rx3.match('\u0660ab') is None			# 因为编译时设置了flags=re.A，不能匹配非ASCII码
True
"""