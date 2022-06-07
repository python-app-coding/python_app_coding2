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


def gen1b():
    """
    有限迭代生成器的生成器函数

    >>> g = gen1b()
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
g2 = (j for j in range(1, 10, 2))


def gen3(start=1, step=1):
    """
    等距数列生成器
    >>> g = gen3(10, 2)
    >>> [next(g) for _ in range(5)]
    [10, 12, 14, 16, 18]
    >>> g.send(1)
    1
    >>> [next(g) for _ in range(4)]
    [2, 3, 4, 5]
    """
    a = start
    while True:
        input_step = yield a
        a = a + step
        if input_step is not None:
            step = input_step
            a = 1


def gen3b(init_step=0, end=100):
    """
    Fibonacci Sequence with step: an = an-1 + an-1 + step

    >>> g = gen3b()
    >>> [next(g) for _ in range(6)]
    [1, 1, 2, 3, 5, 8]
    >>> g.send(3)
    10
    >>> [g.send(5)] + [next(g) for _ in range(5)]
    (1, 1, 7, 13, 25, 43)
    """
    a, b = 1, 1
    yield a
    yield b
    while a < end:
        a, b = b, a + b + init_step
        input_step = yield b
        if isinstance(input_step, int):
            a, b = 1, 1
            yield a
            yield b
            init_step = input_step


if __name__ == '__main__':
    g1b = gen1b()
    try:
        for _ in range(5):
            print(next(g1b))
    except StopIteration as e:
        print("iter stop", e)

    # 迭代生成器推导式
    for _ in range(3):
        print(next(g2))

    g3b = gen3b()
    print([next(g3b) for _ in range(6)])
    print([g3b.send(1)] + [next(g3b) for _ in range(5)])
