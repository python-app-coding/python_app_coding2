# coding: utf8

"""
函数定义示例：
>>> def sum_power(a, b=1, c=1):	# 函数名为sum_pow，a为位置参数，b、c为关键字参数
...     \"\"\"计算三个参数和的平方\"\"\"	# 函数说明文档
...     x = (a+b+c)**2		            # 函数语句
...     return x		                # 函数返回值

函数定义后，Python解释器将其视为一个对象：
>>> type(sum_power)	# sum_power是一个类型为function的对象
<class 'function'>

使用帮助命令可以获取函数的说明文档：
>>> help(sum_power)         # __main__ if running at interpreter
Help on function sum_power in module sec57_func:
<BLANKLINE>
sum_power(a, b=1, c=1)
    计算三个参数和的平方
<BLANKLINE>

调用函数：
>>> sum_power(10, 20)	# 根据位置将10，20分别赋值给a、b，而c使用默认值1
961

>>> sum_power(1, c=2)	# a赋值1，b使用默认值1，c赋值2
16

使用解包方式给参数赋值：
>>> r = [1, 2]
>>> w = {'c': 3}
>>> sum_power(*r, **w)	# 以解包方式传递数据给位置和关键字参数
36


【函数调用】
（1）根据赋值方式参数分为位置参数和关键字参数。
>>> def fun(x, y=1):		# x为位置参数，y为关键字参数
...     print(x, y)

关键字参数在位置参数之前定义，触发异常
# >>> def fun2(x=1, y):
#
#   File "<ipython-input-7-838cdf34aa67>", line 1
#     def fun2(x=1, y):
#                    ^
# SyntaxError: non-default argument follows default argument

（2）调用函数时，位置参数可以按照参数所在位置对应赋值，不需要指定参数名。位置参数可以使用参数名称进行赋值，相当于关键字参数。
>>> fun(3)		# 位置参数直接按照位置赋值，关键字参数不赋值，使用缺省值
3 1
>>> fun(x=3)		# 使用关键字参数赋值
3 1

3）使用关键字参数赋值时，关键字参数之间位置可以忽略：
>>> fun(y=2, x=3)	# 使用关键字参数赋值，位置可以在后面
3 2

不能在关键字参数之后使用位置参数赋值，函数不能判断参数位置，触发语法异常SyntaxError。
# >>> fun(y=2, 3)		# 作为位置参数，位置不能改变，否则触发语法异常SyntaxError
# File "<ipython-input-6-f9985fff4ba4>", line 1
#     fun(y=2, 3)
#               ^
# SyntaxError: positional argument follows keyword argument

4）关键字参数前面的参数都按照位置参数使用，则该参数也可以按照位置参数使用，即不使用参数名称赋值。
>>> def fun3(x, y=1, z=1):
...     return x + y + z
>>> fun3(1,2,3)		# x和y都使用位置方式赋值，z也可以使用位置赋值
6

5）可以使用解包方式定义参数。
>>> def fun4(*x, **y):
...     return sum(x)+sum(y.values())
>>> fun4(1)
1
>>> fun4(1, 2, 3, x=5)
11
>>> a, b = [1, 2, 3], {'a': 10, 'b': 20}
>>> fun4(*a, **b)
36

6）可以使用解包方式给参数赋值。
在参数赋值中，使用解包方式，可以将序列按照位置赋值给参数，将字典按照名称赋值给参数。
>>> def fun5(x, y=1, z=1):
...      return (x + y) * z
>>> a = (1, 2, 3)
>>> fun5(*a)
9
>>> b = {'x': 10, 'z': 20}
>>> fun5(**b)		# 通过解包，将字典以x=10,z=20的方式赋值给参数
220

使用解包赋值参数时，序列必须与参数的位置相对应，字典中的键必须在函数参数中能够找到匹配的关键字参数，否则会触发异常。
# >>> a = (1, 2, 3， 4)
# >>> fun5(*a)
# ...
# TypeError: fun5() takes from 1 to 3 positional arguments but 4 were given
# >>> b = {'x': 10, 'z': 20, 'w': 100}
# >>> fun5(**b)
# ...
# TypeError: fun5() got an unexpected keyword argument 'w'
"""