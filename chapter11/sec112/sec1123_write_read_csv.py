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

    """


def demo3_column_type():
    """

    """