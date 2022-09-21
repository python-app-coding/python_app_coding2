# coding = utf8


def div1(x, y):
    """
    # 未触发异常时，执行语句x/y，及else部分代码
    >>> div1(1, 2)
    'x / y = 0.50'

    # 出现可以处理的异常时，打印异常变量，返回处理该异常后的信息
    >>> div1(1, 0)
    zderror:  division by zero
    '1/0 raise ZeroDivisionErro!'

    """
    try:
        x/y
    except ZeroDivisionError as zderror:
        print("zderror: ", zderror)
        return '{}/{} raise ZeroDivisionErro!'.format(x, y)
    else:
        return 'x / y = {:.2f}'.format(x/y)


def div2(x, y):
    """
    # 除数为0时，触发ZeroDivisionError的 提示
    >>> div2(1, 0)
    'Zero division or type error: division by zero'

    # 数据类型不能进行运算时，触发TypeError的提示
    >>> div2(1, '3')
    "Zero division or type error: unsupported operand type(s) for /: 'int' and 'str'"

    """
    try:
        x/y
    except (ZeroDivisionError, TypeError) as e:	# 捕获除0或类型错误异常,保存到e
        return 'Zero division or type error: {}'.format(e)
    else:
        return 'x / y =3 {:.2f}'.format(x/y)


def div3(x, y):
    """
    针对出现的不同异常，执行匹配的语句：
    >>> div3(1, 0)	# 除数为0时，触发ZeroDivisionError的 提示
    'divided by zero error: division by zero'

    # 数据类型不兼容导致不能进行运算时，触发TypeError的提示
    >>> div3(1, '3')
    "type incompatible error: unsupported operand type(s) for /: 'int' and 'str'"
    """
    try:
        x/y
    except ZeroDivisionError as e1:	    # 捕获除0或类型错误异常,保存到e1
        return 'divided by zero error: {}'.format(e1)
    except TypeError as e2:		        # 捕获除0或类型错误异常,保存到e2
        return 'type incompatible error: {}'.format(e2)
    else:
        return 'x / y =3 {:.2f}'.format(x/y)


def div4(x, y):
    """
    >>> div4(1, 2)
    x/y = 0.50
    Test division operation 1/2

    >>> div4(1, 0)
    division by zero
    Test division operation 1/0
    """
    try:
        a = x/y
    except ZeroDivisionError as e:
        print(e)
    else:
        print('x/y = {:.2f}'.format(x/y))
    finally:
        print('Test division operation {}/{}'.format(x, y))


def div5(x, y):
    """
    >>> div5(1, '2')
    unsupported operand type(s) for /: 'int' and 'str'
    Test division operation 1/2

    """
    try:
        a = x/y
    except ZeroDivisionError as e:
        print(e)
    else:
        print('x/y = {:.2f}'.format(x/y))
    finally:
        print('Test division operation {}/{}'.format(x, y))


if __name__ == '__main__':
    try:
        div5(1, '2')
    except TypeError as e:
        print("outer: ", e)
