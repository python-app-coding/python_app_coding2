# coding = utf8

import time


def time_struct():
    """
    >>> def count_time():
    ...     start = time.time()
    ...     a = sum(range(100000))
    ...     c = time.time() - start
    ...     print('consumed time = {:.4f}'.format(c))
    >>> count_time()    # no expected stable result
    consumed time = 0.0030

    # 一个模拟耗费时间的函数
    >>> def do_something(secs=1):
    ...     time.sleep(secs)

    # 测试执行do_something耗费的时间
    >>> def count_time2():
    ...      start = time.time()
    ...      do_something(0.1)
    ...      c = time.time() - start
    ...      print('consumed time = {:.4f}'.format(c))
    >>> count_time2()       # maybe the result is little larger
    consumed time = 0.1000
    """
