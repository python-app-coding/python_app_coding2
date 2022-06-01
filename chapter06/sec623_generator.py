# coding: utf8


def gen1():
    """
    可无限迭代生成器的生成器函数

    >>> g1 = gen1()
    >>> for j in range(5):
    ...     print(next(g1))
    0
    1
    too big
    too big
    too big
    """
    start = 0
    while True:
        yield start if start < 2 else 'too big'
        start += 1


def gen2():
    """
    有限迭代生成器的生成器函数

    >>> g = gen2()
    >>> try:
    ...     for j in range(5):
    ...         print(next(g))
    ... except StopIteration as e2:
    ...     print(e2)
    0
    1
    2
    <BLANKLINE>
    """
    start = 0
    while start < 3:
        yield start
        start += 1


# 也可以使用(j for j in range(1,3))
g3 = (j for j in [1, 2])


def gen4(para=0):
    a, b = 1, 1
    while True:
        if para < 0:
            print(para)
            a, b = 1, 1
        yield a
        a, b = b, a+b+para


if __name__ == '__main__':
    g2 = gen2()
    try:
        for _ in range(5):
            print(next(g2))
    except StopIteration as e:
        print("iter stop", e)

    # for _ in range(5):
    #     print(next(g3))

    print("methods of g2:")
    print(dir(g2))

    print("methods of g3:")
    print(dir(g3))

    g4 = gen4()
    print([next(g4) for _ in range(4)])
    print(g4.send(-1))
    print([next(g4) for _ in range(4)])
