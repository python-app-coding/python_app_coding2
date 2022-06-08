# coding = utf8

import numpy as np


def demo1():
    """
    >>> persons = [('Wang', 18, 120), ('Li', 20, 150)]		# Python数据：姓名、年龄、身高
    >>> pdata = np.array(persons, dtype='U10, i2, int16')		# 使用复合类型定义一个数组
    >>> pdata
    array([('Wang', 18, 120), ('Li', 20, 150)],
          dtype=[('f0', '<U10'), ('f1', '<i2'), ('f2', '<i2')])
    """


def demo2():
    """
    >>> persons = [('Wang', [18, 120]), ('Li', [20, 150])]	# Python数据

    >>> pdata = np.array(persons, dtype='U10, 2uint8')		# 使用嵌套复合类型

    # >>> pdata = np.array(persons, dtype='U10, 2uint8')	# 也可以使用长类型名称

    >>> pdata
    array([('Wang', [ 18, 120]), ('Li', [ 20, 150])],
          dtype=[('f0', '<U10'), ('f1', 'u1', (2,))])

    >>> pdata[1]					# 数组的每个元素是一个复合类型
    ('Li', [ 20, 150])
    >>> pdata.shape
    (2,)
    """

def demo3():
    """
    # 学生成绩数据
    >>> data = [
    ...        ('Zhai Linwei', 80, 87, 92, 259),
    ...        ('Zhou Geshan', 90, 80, 88, 258),
    ...        ('Zang Keting', 67, 73, 70, 210),
    ...        ]

    # 逐列进行命名、类型定义
    >>> score_type = np.dtype([('name', 'U20'),
    ...                        ('science', 'u1'),
    ...                        ('math', 'u1'),
    ...                        ('physics', 'u1'),
    ...                        ('total', 'u2')])

    # 由复合结构创建学生信息多维数组
    >>> students = np.array(data, dtype=score_type)

    # 引用字段数据进行计算
    >>> students['science'].max()	# 计算science的最大值
    90
    >>> students['math'].mean()		# 计算math的平均值
    80.0
    >>> students['total'].std()	 	# 计算total的标准差
    22.866763848189994
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
