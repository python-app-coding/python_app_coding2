# coding = utf8

import pandas as pd


def demo0():
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


def demo3():
    """
    使用二维序列数据和指定列名称序列，构建DataFrame数据集：
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

    使用列名作为键，可以调用DataFrame的列数据，每个列的数据结构为Series结构：
    >>> df['Mango']
    0    4
    1    5
    2    6
    3    3
    4    1
    Name: Mango, dtype: int64

    以字典方式给出数据，使用键作为列名，字典值作为数据，也可以创建DataFrame。在字典数据中，需要各个值给出的序列的长度相同：
    >>> data={'name': ['Zhai Linwei', 'Zhou Geshan', 'Zang Keting'],
    ...       'yw': [80, 90, 67],
    ...	      'sx': [87, 80, 73],
    ...	      'wy': [92, 88, 70],
    ...       'zf': [259, 258, 210]}
    >>> index = ['a','b','c']
    >>> df = pd.DataFrame(data=data, index=index)
    >>> df
              name  yw  sx  wy   zf
    a  Zhai Linwei  80  87  92  259
    b  Zhou Geshan  90  80  88  258
    c  Zang Keting  67  73  70  210
    """