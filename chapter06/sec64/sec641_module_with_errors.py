# coding: utf8

x = y + 100		        # 导入时会提示变量y没有找到错误
y = 10
z = fun(10, 2)		    # 导入时会提示函数fun未定义错误
w = MyClass()		    # 导入时会提示类MyClass未定义错误


def fun(a, b=2):		# 模块函数
     obj = Class()	                    # 定义中的引用不提示错误
     return a**b


class MyClass:		    # 模块类
    def __init__(self):
        print('my class initialized!')	    # 类实例化为对象时，初始化时运行的代码


print('import succeed!')
