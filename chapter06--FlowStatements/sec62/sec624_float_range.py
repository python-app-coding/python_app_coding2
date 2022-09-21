# coding: utf8


class FloatRange:
    """
    功能与range基本相同，可使用浮点数步长。

    >>> v1 = FloatRange(1.5, 10.5, 1.2)

    # 从可迭代对象得到迭代器
    >>> for x in v1:
    ...     print('{:.3f}'.format(x), end=',')  # 以保留3位小数输出，不换行，间隔空格
    1.500,2.700,3.900,5.100,6.300,7.500,8.700,9.900,

    >>> v2 = FloatRange(step=1.5)

    # 使用解包方式完成迭代
    >>> [*v2]
    [0, 1.5, 3.0, 4.5, 6.0, 7.5, 9.0]

    >>> v1[2]
    3.9
    """

    def __init__(self, start=0, stop=10, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):  # 实现__iter__方法，使实例对象可迭代
        _next = 0
        while True:
            result = self.start + _next
            if result >= self.stop:
                break
            yield result
            _next += self.step

    def __getitem__(self, item):
        result = self.start + item*self.step
        if result < self.stop:
            return result
        else:
            raise ValueError
