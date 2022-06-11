# coding = utf8

import numpy as np
import pandas as pd


def demo1_to_csv():
    """
    >>> df = pd.DataFrame(
    ...           data={'name':['Zhai Linwei','Zhou Geshan','Zang Keting'],
    ...                 'yw':[80,90,67],
    ...                 'sx':[87,80,73],
    ...                 'wy':[92,88,70],
    ...                 'zf':[259,258,210]},
    ...           index=['0101','0102','0103'])
    >>> df
                 name  yw  sx  wy   zf
    0101  Zhai Linwei  80  87  92  259
    0102  Zhou Geshan  90  80  88  258
    0103  Zang Keting  67  73  70  210

    # 使用数据集方法to_csv写csv文件
    >>> df.to_csv('temp.csv')

    # csv file content:
    ,name,yw,sx,wy,zf
    0101,Zhai Linwei,80,87,92,259
    0102,Zhou Geshan,90,80,88,258
    0103,Zang Keting,67,73,70,210
    """


def demo2_read_csv():
    """
    >>> df2 = pd.read_csv('temp.csv')

    # 由于没有指定index,原索引标签被作为第一列读出
    # 在标题行中没有第一列的名称，赋予一个临时名称
    >>> df2
       Unnamed: 0         name  yw  sx  wy   zf
    0         101  Zhai Linwei  80  87  92  259
    1         102  Zhou Geshan  90  80  88  258
    2         103  Zang Keting  67  73  70  210
    """


def demo3_column_type():
    """
    >>> df3 = pd.read_csv('temp.csv', index_col=0, dtype={0: str})

	# 将第一列读出为索引标签，但识别为整数类型, 设置dtype不能限制索引列的推断过程
    >>> df3
                name  yw  sx  wy   zf
    101  Zhai Linwei  80  87  92  259
    102  Zhou Geshan  90  80  88  258
    103  Zang Keting  67  73  70  210

    # 正确读出索引列为字符类型，需要先按照设置类型读出列，然后置为索引列
    >>> df4 = pd.read_csv('temp.csv', dtype={'sno': str},
    ...                   header=0, names=['sno', 'name', 'yw', 'sx', 'wy', 'zf'])
    >>> df4
        sno         name  yw  sx  wy   zf
    0  0101  Zhai Linwei  80  87  92  259
    1  0102  Zhou Geshan  90  80  88  258
    2  0103  Zang Keting  67  73  70  210

    # 重置索引
    >>> df4 = df4.set_index('sno')
    >>> df4
                 name  yw  sx  wy   zf
    sno
    0101  Zhai Linwei  80  87  92  259
    0102  Zhou Geshan  90  80  88  258
    0103  Zang Keting  67  73  70  210
    """


def demo4_dtypes():
    """
    # 根据数据情况设置类型
    >>> df5 = pd.read_csv(
    ...		'temp.csv',
    ...		 dtype={'yw':np.uint8,
    ...		        'sx':np.uint8,
    ...		        'wy':np.uint8,
    ...		        'zf':np.uint16,
    ...		        'name':str,
    ...		        'sno':np.str_},
    ...       header=0,
    ...       names=['sno', 'name', 'yw', 'sx', 'wy', 'zf']
    ...		  )
    >>> df5 = df5.set_index('sno')	# 使用数据列Unnamed: 0重设索引

    # 存储空间大量减少
    >>> df5.info()
    <class 'pandas.core.frame.DataFrame'>
    Index: 3 entries, 0101 to 0103
    Data columns (total 5 columns):
     #   Column  Non-Null Count  Dtype
    ---  ------  --------------  -----
     0   name    3 non-null      object
     1   yw      3 non-null      uint8
     2   sx      3 non-null      uint8
     3   wy      3 non-null      uint8
     4   zf      3 non-null      uint16
    dtypes: object(1), uint16(1), uint8(3)
    memory usage: 63.0+ bytes

    >>> df5.to_csv('temp_csv_file_2.csv')
    >>> df5.index
    Index(['0101', '0102', '0103'], dtype='object', name='sno')

    >>> df6 = pd.read_csv('temp_csv_file_2.csv', dtype={'sno': np.str_})		# 读出存储后的文件内容
    >>> df6
        sno         name  yw  sx  wy   zf
    0  0101  Zhai Linwei  80  87  92  259
    1  0102  Zhou Geshan  90  80  88  258
    2  0103  Zang Keting  67  73  70  210
    """