# coding: utf8

"""
【元组创建和应用示例】
>>> x = tuple(range(10))	#生成元素为0-9的元组
>>> x[0], x[5], x[-1]	# 使用下标访问序号为0,5,-1的元素，以逗号分隔的对象结果为元组
(0, 5, 9)


【元组不可改变】
>>> x[0] = 10		# 给元组的元素再赋值会触发异常
Traceback (most recent call last):
    ...
TypeError: 'tuple' object does not support item assignment

【元组的可变元素可以改变】
如果一个元组的某个元素是可变的，那这个元素的内容可以改变，这个元素名（标识）不能改变。
>>> x = (1,2,[1])
>>> 'id', id(x[2])            # doctest: +ELLIPSIS
('id', ...)

>>> x[2][0] = 10	    # 使用下标访问运行修改，赋值是针对列表
>>> x	                # 作为元素的列表内容发生了改变，但该列表的id没有改变
(1, 2, [10])

>>> 'id', id(x[2])      # doctest: +ELLIPSIS
('id', ...)

【奇异改变】
在编程中要尽量避免在不可修改容器类型内放置可变类型元素，尤其使嵌套组合的元素，混合使用会造成难以预料的计算结果。
将第2个元素进行+运算，改变了对象，将触发异常  # 元组对象不支持元素修改
>>> x[2] += [2]
Traceback (most recent call last):
  ......
TypeError: 'tuple' object does not support item assignment

但元组的内容仍然发生了改变
>>> x
(1, 2, [10, 2])


【隐形元组】
运算式中使用都会分隔的多个对象，如果不在其它序列内部（如在[]或{}内部），其运算值就是元组。
>>> a = 1, 'P', 3
>>> a
(1, 'P', 3)


【元组解包】
 对右边序列的解包（unpacking）
 >>> a, b, c = range(3)
 >>> a
 0
 >>> b
 1
 >>> c
 2

使用*作为某个变量的前缀，可以接收序列中不明确个数的元素
>>> a, *b, c = range(5)	# 带有*前缀的变量b接收序列中不明确个数的元素，变量a,c接收单个元素
>>> a, b, c
(0, [1, 2, 3], 4)
>>> a, b, *c = range(5)	# c放在末尾，接收最后的不确定个数元素
>>> a, b, c
(0, 1, [2, 3, 4])

但是，在被赋值的变量序列中，只能有一个变量带有*前缀，否则无法为两个元组确定元素，会触发异常。
>>> a, *b, *c = range(5)	# 无法确定b和c的元素	#语法错误：使用了多个*表达式
Traceback (most recent call last):
...
SyntaxError: multiple starred expressions in assignment

使用拆包运算，还可以实现变量交换的优雅方式：
>>> a, b = b, a

【命名元组】
命名元组创建和操作示例：
>>> from collections import namedtuple
>>> Score = namedtuple('MyScore', ['lang', 'math', 'sci'])
>>> sc1 = Score(100, 80, 60)
>>> sc1
MyScore(lang=100, math=80, sci=60)
>>> sc1.math
80
>>> sc1[2]
60
"""