# coding: utf8

"""
在PEP8中提出了一些编写代码的推荐方式，使编写的代码具有更明确的语义，也更符合Python的编程原则。下面是其中最常遇到的编写代码时需要处理好的表达形式。

（1）如果与一个单例对象进行比较，如None，尽量使用is，而不使用==。
>>> foo = None

正确方式:
>>> if foo is None: print("Ok")
Ok

错误方式:
>>> if foo == None: print("No")
Ok

（2）进行判断是否为None时，要使用is not None，不要使用not <object> is None。
正确方式:
>>> if foo is not None: print("Ok")

错误方式:
>>> if not foo is None: print("No")

（3）如果定义一个有名称的函数，尽量使用def，而不使用lambda。lambda语句主要用于嵌入到其他语句之中的匿名函数，不是单独定义有名称的函数。
正确方式:
def f(x):
     return 2*x

错误方式:
f = lambda x: 2*x

（4）保持return语句的一致性，存在多个return语句时，或者都返回明确的值，或者都不返回。
正确方式:
def foo(x):
     if x >= 0:
          return math.sqrt(x)
     else:
          return None

def bar(x):
     if x < 0:
          return None
     return math.sqrt(x)

错误方式:
def foo(x):
     if x >= 0:
          return math.sqrt(x)

def bar(x):
     if x < 0:
          return
     return math.sqrt(x)

（5）不将逻辑值与True进行比较。
>>> greeting = True

正确方式：
>>> if greeting: print("Welcome!")
Welcome!

错误方式：
>>> if greeting == True: print("Error Mode!")
Error Mode!

更差的方式：
>>> if greeting is True: print("Bad Mode!")
Bad Mode!
"""
