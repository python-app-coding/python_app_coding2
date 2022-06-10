# coding = utf8


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
    >>> df.to_csv('temp_csv_file_1.csv')

    # csv file content:
    ,name,yw,sx,wy,zf
    0101,Zhai Linwei,80,87,92,259
    0102,Zhou Geshan,90,80,88,258
    0103,Zang Keting,67,73,70,210
    """


def demo2_read_csv():
    """
    >>> dfread = pd.read_csv('temp_csv_file_1.csv')

    # 由于没有指定index,原索引标签被作为第一列读出
    # 在标题行中没有第一列的名称，赋予一个临时名称
    >>> dfread
       Unnamed: 0         name  yw  sx  wy   zf
    0         101  Zhai Linwei  80  87  92  259
    1         102  Zhou Geshan  90  80  88  258
    2         103  Zang Keting  67  73  70  210
    """


def demo3_column_type():
    """
    >>> dfscore = pd.read_csv('student_score.csv'，index_col=0)

	# 将第一列读出为索引标签，但识别为整数类型
    >>> dfscore
                name  yw  sx  wy   zf
    101  Zhai Linwei  80  87  92  259
    102  Zhou Geshan  90  80  88  258
    103  Zang Keting  67  73  70  210
    """