# coding: utf8

"""
贪婪与懒惰模式

>>> import re

表达式成功匹配后仍然搜索，产生更长的匹配结果：
>>> ps1 = r'\|.*\|'
>>> re.search(ps1,'|a|bbb|c|')	    # 成功匹配|a|后，仍然扩大匹配
<re.Match object; span=(0, 9), match='|a|bbb|c|'>
>>> ps2 = r'\|.+\|'
>>> re.search(ps2,'|a|bbb|c|')	    # '+'控制符也使用贪婪策略
<re.Match object; span=(0, 9), match='|a|bbb|c|'>


改变匹配范围或增加匹配边界限制，可以阻止贪婪：
>>> ps3 = r'\|\w*\|'
>>> re.search(ps3,'|a|bbb|c|')	            # 贪婪不仅缘于'+'和'*'，也与'.'的贪婪相关
<re.Match object; span=(0, 3), match='|a|'>
>>> ps4 = r'\|.*\|b'
>>> re.search(ps4,'|a|bbb|c|')	            # 仍然使用'.'匹配，'b'限定了贪婪
<re.Match object; span=(0, 3), match='|a|b'>


使用'?'改变为懒惰模式：
>>> ps5 = r'\|\w*?\|'
>>> re.search(ps4,'|a|bbb|c|')		        # 限定匹配次数，实现懒惰方式
<re.Match object; span=(0, 3), match='|a|'>
>>> ps5 = r'<.*>'
>>> re.search(ps5,'<a>b<c>')
<re.Match object; span=(0, 7), match='<a>b<c>'>
>>> ps6 = r'<.*?>'
>>> re.search(ps6,'<a>b<c>')
<re.Match object; span=(0, 7), match='<a>'>


在服从匹配成功的全局目标下具备懒惰设置会失效：
>>> ps7 = r'<.*?>d'
>>> re.search(ps7,'<a>b<c>d')	# 为了整体匹配，仍然多次匹配'.'
<re.Match object; span=(0, 7), match='<a>b<c>d'>
"""