# coding = utf8

"""
>>> import time
>>> from functools import wraps

# 原函数：
>>> def test1():
...    \"\"\"计算平方和\"\"\"
...    return sum([x**2 for x in range(n)])

# 原函数的名称和注释文档属性值：
>>> test1.__name__
'test1'
>>> test1.__doc__
'计算平方和'


# 被装饰后，原函数的名称和注释文档属性值：
>>> test1.__name__
'test1'
>>> test1.__doc__
'计算平方和'

# 装饰函数
>>> def printtime(fun):
...    def run():
...        start = time.time()
...        result = fun()
...        print('time = {:.4f}'.format(time.time()-start))
...        return result
...    return run


# 增加打印时间功能装饰器：
>>> @printtime
... def test1():
...     \"\"\"计算平方和\"\"\"
...     return sum([x**2 for x in range(n)])


# 可以通过在装饰器函数中增加一些代码，来解决这个问题：
>>> def printtime(fun):
...     def run():
...         start = time.time()
...         result = fun()
...         print('time = {:.4f}'.format(time.time()-start))
...         return result
...     run.__name_ = fun.__name__
...     run.__doc__ = fun.__doc__
...     return run


# 更好的方式是，在装饰器的装饰函数上，使用Python模块functools提供的wraps装饰器：
>>> def printtime_wraps(fun):
...     @wraps(fun)
...     def wrapper():
...         start = time.time()
...         result = fun()
...         print('time = {:.4f}'.format(time.time()-start))
...         return result
...     return wrapper


# 重新装饰test函数：
>>> @printtime_wraps
... def test4(n=100000):
...     \"\"\"计算平方和\"\"\"
...     return sum([x**2 for x in range(n)])


使用functiontools.wraps装饰，查看被装饰函数的属性：
>>> test4.__name__
'test4'
>>> test4.__doc__
'计算平方和'

使用wraps改进装饰器，还可以保证使用help时，调用原函数的签名：
>>> help(test4)
Help on function test4 in module sec638_dec_by_wraps:
<BLANKLINE>
test4(n=100000)
    计算平方和
<BLANKLINE>
"""
