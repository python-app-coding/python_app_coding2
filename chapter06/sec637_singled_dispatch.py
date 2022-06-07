# coding = utf8

"""
单分派编程方式：
from functools import singledispatch

@singledispatch
def basefun(arg):		        # 单分派主函数
    pass


@basefun.register(vartyp)		# 绑定到主函数basefun的函数
def _(arg):
    pass


@basefun.register		        # Python 3.7之后的版本中，可以使用类型注释的方式绑定
def _(arg: vartype):
    pass
"""


# 单分派编程方式：
from functools import singledispatch


# 单分派编程示例：
@singledispatch
def add12(x, y):
    return x + y


@add12.register(list)
def _(x: list, y):
    return [v1+v2 for v1, v2 in zip(x, y)]


@add12.register
def _(x: tuple, y):
    return tuple(v1+v2 for v1, v2 in zip(x, y))


# 调用单分派函数：
print(add12(2, 3))
# 5
print(add12([2, 3], [1, 2]))
# [3, 5]
print(add12((2, 3), [1, 2]))
# (3, 5]