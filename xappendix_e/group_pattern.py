# coding: utf8

"""
在括号中使用'？'和'#'组合开始，表示一个注释。该分组不参与匹配，括号中内容被忽略，并且不作为分组空匹配返回。

>>> import re

【模式】
(?#...)
【示例】
>>> result = re.match('[A-Z]\w+(?#match capital+any letters)', 'BBC animal video')
>>> result.group()
'BBC'

【模式】
(?aiLmsux)
其中，各标志字母分别为：a：re.A，i：re.I，L：re.L，m：re.M，s：re.S，u：re.U，x：re.X。
该组本身不匹配任何模式，也称为非捕获组。该分组必须置于模式的开始。
在Python3中，匹配字符串时，不允许使用re.L的标志限定本地字符集。
【示例】
>>> re.match('(?i)[a-z]+', 'aBc ef')
<re.Match object; span=(0, 3), match='aBc'>

【模式】
(? : ...)

【示例】
>>> r = re.match('(?:\d+)(\w{3})', '123456abcd')
>>> print(r)		            # (?:\d+)分组参与了匹配
<re.Match object; span=(0, 9), match='123456abc'>
>>> r.groups()					# 分组匹配结果中没有(?:\d+)分组
('abc',)
>>> r.group(0,1)				# 分组匹配中存在组合匹配结果
('123456abc', 'abc')

【模式】
(?aiLmsux-imsx:...)
【示例】
# 在第一分组内限制忽略大小写，第一分组使用'?i'标志，忽略大小写进行匹配
>>> r = re.match('(?i:[a-z]{3})(?:\w{2})([a-zA-Z]+)', 'AbC汉字bcD')
>>> print(r)
<re.Match object; span=(0, 8), match='AbC汉字bcD'>

# 在分组内使用'？-i'，去除了由flags=re.I设置的忽略大小写作用
>>> re.match('(?-i:[a-z]+)', 'aBc', flags=re.I)
<re.Match object; span=(0, 1), match='a'>

【模式】
(?P<name>...)
【示例】
# 命名两个分组g1和g2：(?P<g1>[a-zA-Z]{3})、(?P<g2>\w{2})
>>> r=re.match('(?P<g1>[a-zA-Z]{3})(?P<g2>\w{2})([a-zA-Z]+)', 'AbC汉字bcD')

# 各分组匹配结果
>>> r.groups()
('AbC', '汉字', 'bcD')

# 使用名称g1提取分组匹配结果
>>> r.group('g2')
'汉字'

# 使用标号引用，与命名提取结果相同
>>> r.group(2)
'汉字'
>>> r.group(3)	# 使用标号引用
'bcD'

# 更复杂的分组匹配情况
>>> mr = re.match('(?P<word>\w+) (?P<number>[0-9]+(\w+)?)', 'week 03 is next')
>>> mr.groups()	    # 3分组未使用
('week', '03', None)
>>> mr.groups(101)	# 为3分组设置值101
('week', '03', 101)
>>> mr.groupdict()	# 方法groupdict返回组名和匹配值为键值对的字典
{'word': 'week', 'number': '03'}


在三种情况下，可以使用组名称对组进行引用：
a.在匹配模式中，进行后向引用，引用方式为：(?P=name)；
b.在匹配结果中，使用group方法引用，如：group(name)；
c.在替换方法re.sub的repl参数中，使用分组引用，如：'\g<name>'。
在同一模式中对后面定义的组进行引用时，要注意被引用组使用后面引用组的匹配结果进行匹配，而不是使用引用组的模式进行重新匹配。
【示例】
# 后向引用设置：(?P=g1)后向引用分组g1
>>> r = re.match('(?P<g1>[a-zA-Z]{3})\w{2}(?P=g1)', 'AbC汉字AbC')
>>> print(r)	# 结果都是AbC
<re.Match object; span=(0, 8), match='AbC汉字AbC'>
>>> r.group('g1')				# 匹配结果中使用名称引用组
'AbC'

# 尽管分组g1可以匹配abc，但g1已与AbC匹配，再次匹配时需使用AbC匹配，所以不能匹配abc
>>> re.match('(?P<g1>[a-zA-Z]{3})\w{2}(?P=g1)', 'AbC汉字abc')

# 使用分组g2的匹配结果123，替换匹配串Song-123
>>> re.sub('(?P<g1>[S|f]\S+)-(?P<g2>[0-9]*)', '\g<g2>', 'Song-123 is nice!')
'123 is nice!'


【模式】
(?=...)

【示例】
# 实现前向判断，但判断结果不在匹配结果中
>>> re.match('Isaac (?=Newton)', 'Isaac Newton')		# 匹配结果不包括Newton
<re.Match object; span=(0, 6), match='Isaac '>

# 前向没有邻接Newton，当前匹配不成功
>>> re.match('Isaac (?=Newton)', 'Isaac newton')


【模式】
(?!...)
【示例】
# 包括大小写，前向非匹配Newton
>>> re.match('Isaac (?!-iNewton)', 'Isaac newton')		# 前向未匹配Newton，当前匹配成功
<re.Match object; span=(0, 6), match='Isaac '>


【模式】
(?<=...)

该模式只能用于判断匹配固定长度的匹配模式，不支持 * 、+、{n,m}等变长模式。该模式不支持在字符串开始的匹配，所以尽量不使用match()，而使用.search()。

【示例】
>>> re.search('(?<=abc)de', '123 abcde')		# 匹配abc，后面的匹配de成功
<re.Match object; span=(7, 9), match='de'>
>>> re.search('(?<=abc)de', '123 abbde')		# 分组匹配不成功，后面匹配失效


【模式】
(? < ! ...)
【示例】
>>> re.search('((?<!fill)roll)', 'rockroll')	# 未匹配rock，当前匹配成功
<re.Match object; span=(4, 8), match='roll'>
>>> re.search('((?<!rock)roll)', 'rockroll')	# 匹配rock，当前匹配不成功
>>> re.match('((?<!fill)roll)', 'lookroll')	# 不支持match


【模式】
(?(id/name)yes-pattern|no-pattern)

如，(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)是一个邮箱地址匹配模式，它会匹配‘<user@host.com>’或‘user@host.com’，但不匹配‘<user@host.com’和‘user@host.com>’。

【示例】
# 设置id=(1), yes-pattern='>', no-pattern=$'
# 1组匹配成功，再最后组匹配'>'
>>> pmail = '(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)'
>>> re.search(pmail,'<user@host.com>')
<re.Match object; span=(0, 15), match='<user@host.com>'>

# 1组匹配不成功，结尾匹配也不成功
>>> re.search('(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)','user@host.com>')

# 1组不匹配成功，最后组匹配成功
>>> re.search('(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)','user@host.com')
<re.Match object; span=(0, 13), match='user@host.com'>
"""