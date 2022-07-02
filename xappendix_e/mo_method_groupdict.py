# coding: utf8

"""
groupdict(default=None)
返回包含所有命名的匹配分组的字典，键值为分组名称。参数default用于未参与匹配的分组返回值，默认为None。

>>> import re

【示例】
>>> ps1 =r"(?P<first_name>\w+) (?P<last_name>\w+)"
>>> mo17 = re.match(ps1, "Malcolm Reynolds")

>>> mo17.groupdict()
{'first_name': 'Malcolm', 'last_name': 'Reynolds'}

>>> ps2 =r"(?P<first_name>\w+) (?P<last_name>\w+)(?P<no_match>[0-9]{}2)?"
>>> mo18 = re.match(ps2, "Malcolm Reynolds")

# 未匹配分组使用默认值None
>>> mo18.groupdict()		
{'first_name': 'Malcolm', 'last_name': 'Reynolds', 'no_match': None}

# 未匹配分组使用指定值100
>>> mo18.groupdict(100)		
{'first_name': 'Malcolm', 'last_name': 'Reynolds', 'no_match': 100}
"""