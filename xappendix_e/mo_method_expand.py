# coding: utf8

"""
expand(template)
返回使用模板字符串进行反斜杠替换后的字符串，类似于sub()方法。转义符被转换到相应的字符, 数字反向引用（如\1），
名称反向引用（如\g<1>）, 使用相应的分组内容进行替换。自Python3.5之后，未匹配分组使用空字符串替换（即不替换）。

>>> import re

【示例】
>>> mo16 = re.search('(?P<first_group>a)(b)(\s*)', 'ab')
>>> mo16.groups()
('a', 'b', '')

>>> mo16.expand(r'\g<first_group>\\2c')
'abc'

>>> mo16.expand('\g<first_group>\2c\3\\12')
'a\\x02c\\x03\\n'
"""