# coding = utf8

"""
>>> import types                          	# types模块包含很多Python类型


>>> def fun1(x=1):		# 定义函数fun，完成定义后，提交给交互环境（加载），即生成对象
...    return x**2


>>> isinstance(fun1, types.FunctionType)	    # fun是一个函数类型的对象，对象是在运行时创建的 True
True
>>> print(type(fun1))                           # 函数类对象
<class 'function'>
>>> print(fun1(3))		                        # 调用函数fun，通过赋值参数，函数被实例化，并执行其中代码 9
9

>>> fvar = fun1
>>> print(fun1 is fvar)		            # 两个变量是一个值，即指向相同的值
True
>>> id(fun1) == id(fvar)	            # 变量的id为运行时动态确定，各次运行会不相同
True

>>> def fun2(f):		                # 函数fun2的参数f为一个函数类型，y为数字值
...    return f(2)*3

>>> fun2(fun1)
12

>>> def fun3():  # 定义一个返回值为函数的函数
...
...    def funy(y):  # 在函数内定义函数
...        return y + 2
...
...    return funy

>>> fun4 = fun3()                       # fun3的返回结果为一个函数类型,赋值给变量fun4
>>> fun4(3)                             # fun4实例化并执行其运算代码
5
"""
