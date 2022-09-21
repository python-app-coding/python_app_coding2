# coding = utf8


a = 1000
b = [1, 2, 3]


def para_pass(x, y):
    """
    在函数内部改变序列参数的元素值

    外部变量id:
    >>> print("id(a)=", id(a))
    id(a)=f'{id(a)}'
    >>> print("id(b)=", id(b))
    >>> print("传递a,b给函数参数x, y： para_pass(a, b)")
    >>> para_pass(a, b)

    >>> print("传递前： b = [1, 2, 3]")
    >>> print("传递后： b = {}".format(b))        # 外部变量b发生改变
    >>> print("传递前： a = 1000")
    >>> print("传递后： a = {}".format(a))        # 外部变量a没发生改变
    >>> print("")

    """
    print("函数参数id:")
    print("id(x)=", id(x))
    print("id(y)=", id(y))
    print("内部参数赋值： y[0] = 1000， x = 3000")
    y[0] = 1000
    x = 3000


# 传递可变对象给函数，值发生了改变


# 函数接收两个变量，交换两个参数对象的值：
def swap_value(x, y):
    """
    在函数内部交换参数的值
    如果传递可变对象，对象的值会发生改变

    >>> a1, b1 = 100, 200	    # 外部变量
    >>> swap_value(a, b)        # 传递给函数
    >>> print(a1, b1)	        # 外部变量并没有发生变化，说明传递参数的过程进行了复制，而不是引用
    100 200
    """
    x, y = y, x
