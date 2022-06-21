# coding=utf8


def demo_python():
    """
    >>> import math

    # 求平方根
    >>> print("square root of 2 is ", math.sqrt(2))
    square root of 2 is  1.4142135623730951

    # 求1-100的和
    >>> s = sum(range(1, 101))
    >>> print(f"The sum of 1-100 is {s}")
    The sum of 1-100 is 5050

    # 求1-12345之间平方数的个数
    >>> c = [k for k in range(12345) if math.sqrt(k) == int(math.sqrt(k))]
    >>> print(f"The count of square number of 0-12345 is {len(c)}, [{c[0]}, {c[1]}, {c[2]}, {c[3]}, ...]")
    The count of square number of 0-12345 is 112, [0, 1, 4, 9, ...]
    """

