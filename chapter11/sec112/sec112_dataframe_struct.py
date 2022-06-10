# coding = utf8

import pandas as pd


def demo1():
    """
    >>> data = [[4, 5, 2], [5, 4, 3], [6, 3, 5], [3, 0, 2], [1, 2, 7]]
    >>> columns = ['Mango','Apple','Banana']
    >>> df = pd.DataFrame(data=data, columns=columns)
    >>> df
       Mango  Apple  Banana
    0      4      5       2
    1      5      4       3
    2      6      3       5
    3      3      0       2
    4      1      2       7

    >>> df['Mango']
    0    4
    1    5
    2    6
    3    3
    4    1
    Name: Mango, dtype: int64
    """


def demo2():
    """
    >>> data={'name': ['Zhai Linwei', 'Zhou Geshan', 'Zang Keting'],
    ...       'yw': [80, 90, 67],
    ...	      'sx': [87, 80, 73],
    ...	      'wy': [92, 88, 70],
    ...       'zf': [259, 258, 210]}
    >>> index = ['a','b','c']
    >>> df = pd.DataFrame(data=data, index=index)

    # 各列名称及行标签被设置
    >>> df		
              name  yw  sx  wy   zf
    a  Zhai Linwei  80  87  92  259
    b  Zhou Geshan  90  80  88  258
    c  Zang Keting  67  73  70  210
    """
