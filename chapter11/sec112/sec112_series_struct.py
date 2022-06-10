# coding = utf8

import pandas as pd


def demo1():
    """
    >>> sr1 = pd.Series([1, 2, 3])
    >>> sr1					# 缺省使用整数索引, 数据类型转为为int64
    0    1
    1    2
    2    3
    dtype: int64

    >>> sr2 = pd.Series([1, 2.1, 3], index=list('abc'))	# 使用字符序列作为索引
    >>> sr2					# 数据类型转为float64
    a    1.0
    b    2.1
    c    3.0
    dtype: float64
    """