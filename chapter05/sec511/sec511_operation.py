# coding: utf8

"""
（1）单目运算
运算符只作用于一个对象。

单目运算表达式：
[单目运算符] [操作数]

示例：算术符号运算符+和-。
>>> +(-3)	# 第一个+号为运算符，第二个-号的负数标识符号
-3

（2）双目运算
运算符作用于两个对象。运算过程中，左边的对象作用于右边的对象。在很多运算中，如果左边的对象没有实现相应的运算，会调用右边的对象的反向运算方法。

双目运算表达式：
[操作数1] [双目运算符] [操作数2]

示例：算术运算。
>>> 3 + 2	# +号为运算符，3和2为输入对象
5

（3）三目运算：
运算符作用于三个对象。Python没有为三目运算指定符号类型的运算符，而是使用关键字“if-else”实现三目运算。类似于C语言中的“? - :”方式运算。

三目运算表达式：
[操作数1] [if] [操作数2] [else] [操作数3]

示例：单行if-else求值
>>> b = 10
>>> a = 1 if b else 0	# +号为运算符，3和2为输入对象
>>> a
1

（4）多目运算
接受多个变量返回处理值的代码模式，可以称为多目运算。
>>> (lambda x, y, z: sum([x, y, z]))(3, 3, 2)
8
"""
