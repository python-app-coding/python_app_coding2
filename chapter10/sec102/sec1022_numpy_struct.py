# coding = utf8

import numpy as np


def demo_numpy_struct():
    """
    >>> persons = [('Wang', 18, 120), ('Li', 20, 150)]		# Python数据：姓名、年龄、身高
    >>> pdata = np.array(persons, dtype='U10, i2, i2')		# 使用复合类型定义一个数组
    >>> pdata
    array([('Wang', 18, 120), ('Li', 20, 150)],
          dtype=[('f0', '<U10'), ('f1', '<i2'), ('f2', '<i2')])
    """

def demo2():
    """
    >>> persons = [('Wang', [18, 120]), ('Li', [20, 150])]	# Python数据
    >>> pdata = np.array(persons, dtype='U10, 2u1')		# 使用嵌套复合类型
    >>> pdata
    array([('Wang', [ 18, 120]), ('Li', [ 20, 150])],
          dtype=[('f0', '<U10'), ('f1', '<u2', (2,))])

    >>> pdata[1]					# 数组的每个元素是一个复合类型
    ('Li', [ 20, 150])
    >>> pdata.shape
    (2,)
    """