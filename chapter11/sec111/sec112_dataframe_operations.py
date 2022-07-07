# coding = utf8

"""
展示创建DataFrame数据框

>>> import pandas as pd

使用字典给出源数据
使用默认的整数索引
>>> df1 = pd.DataFrame(
...     data={'sno': ['1001', '1002', '1003'],
...           'name': ['李明', '张力', '韩中'],
...           'score': [95, 88, 98]
...           }
...     )

使用字典给出源数据
指定序列作为索引
>>> df2 = pd.DataFrame(
...     data={'sno': ['1001', '1002', '1003'],
...           'name': ['李明', '张力', '韩中'],
...           'score': [95, 88, 98]
...           },
...     index=list('abc')
...     )

>>> print(df1)
    sno name  score
0  1001   李明     95
1  1002   张力     88
2  1003   韩中     98

>>> print(df2)
    sno name  score
a  1001   李明     95
b  1002   张力     88
c  1003   韩中     98

1. 切片操作
（1）使用下标[]方式，只能针对行序号切片，切片结果中不包括尾部行号对应的行数据。
>>> df1[0:1]		 	# 提取到第0行数据，不包括第1行
... # doctest: +NORMALIZE_WHITESPACE
    sno  name   score
0  1001   李明     95
>>> df2[0:1]			# 索引为字符，不影响行切片
... # doctest: +NORMALIZE_WHITESPACE
    sno  name   score
a  1001   李明     95

（2）使用iloc[]方式，可以针对行或列两个方向的序号切片，切片结果不包括尾部序号数据。
>>> df1.iloc[1:2, 1:3]		# 提取第1行、第1-2列数据，不包括尾部序号数据
... # doctest: +NORMALIZE_WHITESPACE
   name   score
1   张力     88

（3）使用loc方式，针对行、列两个方向进行索引切片，切片结果中包括尾部标签对应的数据。
>>> df2.loc['b':'c', 'name':'score']	# 索引切片，包括了尾部标签对应的数据
... # doctest: +NORMALIZE_WHITESPACE
   name   score
b   张力     88
c   韩中     98

（4）使用iloc[]、iat[]可以使用位置（行列序号）提取数据
如果将DataFrame视为2维数组，可以使用iat[row, col]方式，直接提取对应位置的元素，或对该位置元素重新赋值。
>>> df1.iloc[0, 1]		# 提取到第0行、第1列数据
'李明'
>>> df1.iat[0, 1]		# 提取到第0行、第1列数据
'李明'
>>> df1.iat[0, 2] = 100		# 根据提取位置赋值
>>> df1			# 数据值被改变
... # doctest: +NORMALIZE_WHITESPACE
    sno name  score
0  1001   李明    100
1  1002   张力     88
2  1003   韩中     98

2.条件筛选操作
（1）下标[]方式条件筛选（使用数据集列数据生成布尔序列），只针对行数据的选取。
>>> df1[df1.score>=90]	# 使用列变量建立逻辑表达式，列必须通过数据集名称引用
... # doctest: +NORMALIZE_WHITESPACE
    sno  name   score
0  1001   李明    100
2  1003   韩中     98

（2）loc[]方式条件筛选，选取符合条件的行和列数据。列数据选取时，需要给出选择的列名称序列。
# loc方式可以针对行进行逻辑选择，通过序列指定列名称进行列筛选
>>> df1.loc[(df1.sno > '1001') & (df1.score > 90), ['name', 'score']]
... # doctest: +NORMALIZE_WHITESPACE
   name   score
2   韩中     98


（3）使用query方法实现条件筛选，可以在表达式中直接使用列名，只能选取符合条件的行数据。
>>> df1.query("score>=90 and sno>='1002'")	# 不需要指定数据集名称引用列名
... # doctest: +NORMALIZE_WHITESPACE
    sno  name   score
2  1003   韩中     98

"""
