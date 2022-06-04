# coding = utf8

def max_divisor1(x, y):
    """
    求最大公约数算法（while循环方式）
    Euclid Max_divisor Algorithm（while-loop mode）

    >>> max_divisor1(51, 21)
    3
    >>> max_divisor1(11, 31)
    1
    """
    while True:
        r = x % y
        if r == 0:
            return y
        else:
            x, y = y, r


def max_divisor2(x, y):
     """
     求最大公约数算法（递归方式）
     Euclid Max_divisor Algorithm（recursive mode）

     >>> max_divisor2(21, 51)
     3
     >>> max_divisor2(11, 31)
     1
     >>> max_divisor1(11, 0)
     10
     """
     r = x % y
     return y if r == 0 else max_divisor2(y, r)
