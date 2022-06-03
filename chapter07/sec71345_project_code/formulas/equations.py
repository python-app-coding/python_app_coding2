# coding: utf8
import math
import cmath


def eq12(a, b, c):
    """
    测试代码
    >>> eq12(1, -2, 1)
    (1.0, 1.0)
    """
    delta = b**2 - 4*a*c
    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
    else:
        x1 = complex(-b, math.sqrt(-delta)) / (2*a)
        x2 = complex(-b, - math.sqrt(-delta)) / (2*a)
    return x1, x2


def eq12c(a, b, c):
    """
    求解一元二次方程
    a: 二次元系数
    b：一次元系数
    c：常数项系数
    return: tuple(complex, complex), 方程的两个根
    >>> eq12c(1, -2, 1)
    ((1+0j), (1+0j))
    >>> eq12c(1, 1, 1)
    ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    """
    delta = cmath.sqrt(b**2 - 4*a*c)
    return (-b + delta) / (2*a), (-b - delta) / (2*a)


if __name__ == '__main__':
    # print(eq12(1, 2, 3))
    import doctest
    doctest.testmod(verbose=True)
