# coding: utf8

"""
列表创建及调用示例：
>>> mylist = [1, '1', 12.5]		# 使用中括号包围，可以包含不同元素
>>> s = '学习Python'
>>> list(s)			            # 可以从其他序列生成
['学', '习', 'P', 'y', 't', 'h', 'o', 'n']
>>> x = list(range(10))		    # 生成器range(10)依次生成0-9，list将其类型转为列表
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x[0], x[5], x[-1]		    # 使用下标访问序号为0,5,-1的元素
(0, 5, 9)
>>> x[0] = 10			        # 将序号0的元素赋值为10，改变了该列表
>>> x	                        # 列表已经改变
[10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

列表元素引用变量示例：
>>> a = [1]
>>> b = [a, a, a]		# b的三个元素都引用了a
>>> b
[[1], [1], [1]]
>>> a[0] = 2		# 改变a会影响到b的三个元素
>>> b
[[2], [2], [2]]
>>> a, b = [1], [3]
>>> c = [a, a, b]	# 使用变量a和b作为列表的元素
>>> c
[[1], [1], [3]]
>>> a[0] = 2		# 改变原变量，会改变列表c引用的元素
>>> c
[[2], [2], [3]]

列表的一些基本操作：
（1）可以使用in判断一个对象是否属于列表。
使用in判断对象是否属于列表示例：
>>> mylist = ['1', 2, [3]]
>>> 2 in mylist
True
>>> 1 in mylist
False

（2）内置函数求值
使用函数对列表求值示例：
>>> len(mylist)		# 求序列的长度
3

>>> max(mylist)
Traceback (most recent call last):
...
TypeError: '>' not supported between instances of 'int' and 'str'

>>> mylist2 = [5, 3, 10]
>>> max(mylist2), min(mylist2)
(10, 3)

（3）运算
列表乘法运算示例：
>>> [1] * 3		# 支持与整数的乘法运算
[1, 1, 1]
>>> a = [2]
>>> a *= 3		# 支持*=运算
>>> a
[2, 2, 2]

列表加法运算示例：
>>> [1] + [2]		# 支持列表的加法运算，结果为列表的依次拼接
[1, 2]
>>> a = [2]
>>> a += [3]		# 支持+=运算
>>> a
[2, 3]
"""