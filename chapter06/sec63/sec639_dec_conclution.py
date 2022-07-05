# coding = utf8

"""
# 为了说明多次叠加装饰器顺序问题，设计两个简单的装饰器函数：
>>> def dec1(fun):
...     def wrapper():
...         return fun() + 10
...     return wrapper


>>> def dec2(fun):
...     def wrapper():
...         return fun() * 20
...     return wrapper


# 在同一功能的函数上以不同次序叠加两个装饰器：
>>> @dec1
... @dec2
... def fun21(n=0):		# 效果相当于产生新的函数：dec1(dec2(fun21))
...     return n


>>> @dec2
... @dec1
... def fun12(n=0):		# 效果相当于产生新的函数：dec2(dec1(fun12))
...     return n


# 不同叠加顺序对执行结果会产生影响：
# fun21对应的复合函数：dec1(dec2(test8(n))) = (n * 20) + 10 = 10
# fun12对应的复合函数：dec2(dec1(test9(n))) = (n + 10) * 20 = 200
>>> print(fun21(), fun12())
10 200
"""