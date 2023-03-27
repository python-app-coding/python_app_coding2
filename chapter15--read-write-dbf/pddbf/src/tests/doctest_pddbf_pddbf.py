# coding: utf8
import importlib
import os
import sys

pddbf_path = '../pddbf'
sys.path.insert(0, os.path.abspath(pddbf_path))

pddbf = importlib.import_module('pddbf')


def doctest_read_dbf():
    """
    >>> df = pddbf.read_dbf('dbf_foxpro.dbf')
    >>> df
       a  b
    0  0  x
    1  1  y
    2  2  z

    >>> df2 = pddbf.read_dbf('dbf_with_cn.dbf')
    >>> df2
      serial_no       en_name ch_name   price             shipping
    0     10101  Refrigerator      冰箱  310.51  2020-03-01 01:00:00
    1     10102        Washer     洗衣机  420.35  2020-03-02 01:00:00
    2     10103         Stove      炉子   350.0  2020-03-03 00:30:00
    3     10104    Ventilator     通风机   210.4  2020-03-04 00:00:30

    >>> df3 = pddbf.read_dbf('dbf_with_null.dbf')
    >>> df3
               ksh name      birth                 time  ...   km2      zf    hcf   stat
    0  3702693000a  张同志 2001-01-01  0011-01-01 23:01:02  ...  43.0  107.00  58.75  False
    1  3712091000b  李产生 2001-01-02  1990-01-02 11:01:02  ...  53.0  108.00  54.50  False
    2  37131510000  贺理论 2001-02-01  1901-02-01 00:59:06  ...  62.0  102.00  45.50  False
    3  37077010000  孟自豪 1999-01-01  1999-01-01 01:10:10  ...  52.0   97.00  46.75  False
    4  37015640000  程前进 2010-01-01  2010-01-01 12:01:02  ...  47.0  102.00  53.00  False
    5  37050440000  胡德利 2020-01-01  2020-01-01 12:00:00  ...  35.0   95.00  53.75  False
    6  37085740000  栾作文 1970-01-01  1969-01-01 12:00:00  ...  60.0  121.00  60.75  False
    7  37081250001  苏成绩 1970-02-01  0001-01-01 00:00:00  ...  53.0  108.00  54.50  False
    8  37043430000   成书 1971-01-01  2071-01-01 00:59:59  ...  27.0   84.00  49.50  False
    9  37010100001  end        NaT                 None  ...   0.0   99.99   0.00   True
    <BLANKLINE>
    [10 rows x 9 columns]
    """


if __name__ == '__main__':
    print(pddbf)
