# coding = utf8

import numpy as np


def demo0_dtype_char():
    """
    # 使用dtype(typestr)可以查看各个类型的Numpy对应名称
    >>> np.dtype(np.float_)
    dtype('float64')

    >>> type21 = [np.bool, np.int_, np.intc, np.intp, np.int8, np.int16, np.int32, np.int64,
    ...           np.uint8, np.uint16, np.uint32, np.uint64,
    ...           np.float, np.float16, np.float32, np.float64,
    ...           np.complex_, np.complex64, np.complex128,
    ...           np.str_, np.string_]

    >>> [np.dtype(t).char for t in type21]
    ['?', 'l', 'i', 'q', 'b', 'h', 'l', 'q', 'B', 'H', 'L', 'Q', 'd', 'e', 'f', 'd', 'D', 'F', 'D', 'U', 'S']

    >>> for t in type21:
    ...     print(f'{np.dtype(t).char}: {np.dtype(t).name}')
    ?: bool
    l: int32
    i: int32
    q: int64
    b: int8
    h: int16
    l: int32
    q: int64
    B: uint8
    H: uint16
    L: uint32
    Q: uint64
    d: float64
    e: float16
    f: float32
    d: float64
    D: complex128
    F: complex64
    D: complex128
    U: str
    S: bytes

    >>> [np.dtype(t).str for t in type21[:10]]
    ['|b1', '<i4', '<i4', '<i8', '|i1', '<i2', '<i4', '<i8', '|u1', '<u2']
    >>> [np.dtype(t).str for t in type21[10:]]
    ['<u4', '<u8', '<f8', '<f2', '<f4', '<f8', '<c16', '<c8', '<c16', '<U0', '|S0']
    """



def demo1_tuple_mode():
    """
    # 源数据有4个字段的数据：姓名、年龄、身高、体重
    >>> persons = [('Wang', 18, 156, 60), ('Li', 20, 177, 72)]

    # 定义具有4个字段的复合结构类型：长度为10
    >>> ctype1 = np.dtype([('name', 'U10'),('age', 'i2'), ('height', np.float_),('weight', 'float16')])

    # 使用复合类型创建多维数组
    >>> pdata = np.array(persons, dtype=ctype1)
    >>> pdata
    array([('Wang', 18, 156., 60.), ('Li', 20, 177., 72.)],
          dtype=[('name', '<U10'), ('age', '<i2'), ('height', '<f8'), ('weight', '<f2')])
    """



def demo2_str_mode():
    """
    # 源数据有4个字段的数据：姓名、年龄、身高、体重
    >>> persons = [('Wang', 18, 156, 60), ('Li', 20, 177, 72)]

    >>> pdata = np.array(persons, dtype='U10, i2, float, float16')		# 使用复合类型定义一个数组
    >>> pdata
    array([('Wang', 18, 156., 60.), ('Li', 20, 177., 72.)],
          dtype=[('f0', '<U10'), ('f1', '<i2'), ('f2', '<f4'), ('f3', '<f2')])
    """


def demo3_dict_mode():
    """
    # 源数据有4个字段的数据：姓名、年龄、身高、体重
    >>> persons = [('Wang', 18, 156, 60), ('Li', 20, 177, 72)]

    >>> ctype_dict = {'names': ['name', 'age', 'height', 'weight'],
    ...               'formats': ['U10', 'i2', np.float64, np.float16]
    ...               }

    >>> pdata = np.array(persons, dtype=ctype_dict)
    >>> pdata
    array([('Wang', 18, 156., 60.), ('Li', 20, 177., 72.)],
          dtype=[('name', '<U10'), ('age', '<i2'), ('height', '<f8'), ('weight', '<f2')])
    """


def demo_nest():
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

def demo4():
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
