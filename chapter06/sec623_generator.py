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

    >>> g2 = gen2()
    >>> try:
    ...     for j in range(5):
    ...         print(next(g2))
    ... except StopIteration as e:
    ...     print(e)
    0
    1
    2
    <BLANKLINE>
    """
    start = 0
    while start < 3:
        yield start
        start += 1


g3 = (j for j in [1, 2])	# 也可以使用(j for j in range(1,3))


if __name__ == '__main__':
    g2 = gen2()
    try:
        for _ in range(5):
            print(next(g2))
    except StopIteration as e:
        print("iter stop", e)

    for _ in range(5):
        print(next(g3))
