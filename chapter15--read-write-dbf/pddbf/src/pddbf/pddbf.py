# coding = utf8

import os
import sys
import pandas as pd

curpath = os.path.abspath(os.path.dirname(__file__))
if curpath not in sys.path:
    sys.path.insert(0, curpath)
from dbfreader import DbfReader
from dbfwriter import DbfWriter


def read_dbf(dbffile: str) -> pd.DataFrame:
    """
    读取dbf文件为DataFrame.
    read dbf file to DataFrame.

    :param dbffile: str, dbf file name, suffix .dbf is needed
    :return: DataFrame
    """
    if not os.path.isfile(dbffile):
        raise FileNotFoundError
    dbf = Dbf()
    dbf.open(dbffile)
    dbf.fetch(count=-1)
    dbf.close()
    return dbf.data


def to_dbf(df: pd.DataFrame, dbffile: str):
    """
    将DataFrame数据写为DBF文件.
    write DataFrame to DBF file.

    :param df: 类型为pandas.DataFrame。写入DBF文件的数据。
    :param dbffile: 字符串。写入DBF文件的文件名。
    """
    dbf = Dbf()
    dbf.data = df
    dbf.to_dbf(dbffile)
    dbf.close()


def to_csv(dbf, csv='temp.csv'):
    """
    从dbf文件读出数据，存储到csv文件

    Ags:
        dbf(str): dbf file to read
        csv(str): csv file to write
    """
    df = read_dbf(dbf)
    df.to_csv(csv)


class Dbf:
    """
    ---------------------------------------------------------------------------------------------------------------
    读写DBF文件服务类
    A class used to read and write DBF file，its property data is DataFrame。

    属性:
    data：DataFrame。用于存放读入的DBF文件数据。

    对象方法:
    object methods

    open(self, filename: str = '')
        打开一个DBF文件。用于在方法fetch中读入数据，必须在fetch之前打开。
        open a DBF file, prework for load method
        参数
        :parameters
        filename: str, file name to open

    close()
        关闭打开的DBF文件。当不需要读取DBF文件数据时，可以关闭打开的DBF文件。
        关闭之后，不能使用fetch方法获取数据

    fetch(self, start=1, count=10)
        读入在open方法中打开的DBF文件的数据，存入属性data之中。
        read DBF file data from the file opened in use

        :parameters
        start: int, positive, start record serial number to read from DBF file
        count: int, positive, record count to read from DBF file

    to_csv(self, csvfile='temp.csv', sep=',')
        将数据写入csv文件
        write data to csv file

        :parameters
        csvfile: str. 'temp.csv'( default). file name to write.
        sep: str. ','( default).  length is 1. charater used to seperate field data in record line.

    to_dbf(self, dbffile='exp_foxpro.dbf')
        将数据写入DBF文件
        write data to DBF file

        :parameters
        dbffile: str. 'exp_foxpro.dbf'( default). file name to write.

    ---------------------------------------------------------------------------------------------------------------

    读写DBF文件数据过程说明
    (Explanation about writting DBF file from pandas.DataFrame):

    目前支持的DBF数据类型：

    - C(字符)、N（数值）、F（浮点）、D（日期）、L（逻辑）、T（时间日期）、B（双精度）

    调用方式（call procedure）：

    1. 初始化：          dbf = Dbf()                                 # 创建类Dbf的对象实例
    2. 打开DBF文件：     dbf.open(filename)                           # 打开DBF文件
    3. 读入数据：        dbf.fetch()                                  # 读入DBF文件中的数据
    4. 访问数据          dbf.data                                    # 数据存储在属性变量data，格式为 DataFrame
    5. 写数据csv：       dbf.to_csv(csvname=csvfile，sep=',')        # 将data写到文件csvfile,格式为 csv, 分隔符为sep
    6. 写数据dfb：       dbf.to_dbf(dbfname=dbffile)                 # 将data写到DBF文件

    ---------------------------------------------------------------------------------------------------------------

    数据与接口说明
    (comments for some attributes or interface)

    1. Dbf.data：从DBF文件读入的数据，格式为pandas.DataFrame ( read data to Dbf.data from dbase file)
    2. 从 DBF文件到DataFrame的数据类型转换使用Dbf.type_map，在初始化之前可以查看替换，须保证能够进行类型映射
    3. 对 DBF文件字符内容的解码使用 Dbf.codeset，缺省值为 GBK，初始化之前可以替换
    4. 打开 DBF文件后，可以通过 dbf.file_info查看文件结构信息，通过field_info查看字段结构信息
    5. 读出的数据中包括DBF表的删除和删除标记列，名称为 _delflag、_nullflab，如果原DBF文件中有重名字段，会增加'_'的数量
    6. 切片访问按照切片格式，可以使用下标，小标范围，或索引号, 切片下标使用0开始记录号，而list使用1开始记录号
    7. 写数据到DBF文件，执行结果是将当前data的数据写到一个csv文件。

    ---------------------------------------------------------------------------------------------------------------

    需要注意的问题

    ----------------------

    浮点计算与四舍五入问题
    (some problem about float operation and rounding)

    1. 从dbf文件读入数据时，浮点数转换为Decimal类型
    2. 设置 decimal 舍入格式为 ROUNDING_HALF_UP，精度prec为默认的28位
    3. 从DataFrame写回dbf文件时，对数值型N，根据舍入规则保留小数位数

    标记处理
    (flag field for delete and null flag)

    1. 在从dbf读出数据时，将删除标记读入为一个字段_delflag, 忽略_nullflag
    2. 在向dbf写入数据时，忽略_delflag字段，不写删除标记（所有记录标记 b' '），所有记录标记为未删除

    ---------------------------------------------------------------------------------------------------------------

    调用示例：
    (Examples)

    # read dbf to DataFrame

    >>> dbf = Dbf()
    >>> dbf.open('../tests/demo_with_cn.dbf')
    >>> dbf.fetch(1, 20)
    >>> dbf.data    # doctest: +NORMALIZE_WHITESPACE
          serial_no       en_name ch_name   price            shipping
    0     10101  Refrigerator      冰箱  310.51 2020-03-01 01:00:00
    1     10102        Washer     洗衣机  420.35 2020-03-02 01:00:00
    2     10103         Stove      炉子  350.00 2020-03-03 00:30:00
    3     10104    Ventilator     通风机  210.40 2020-03-04 00:00:30

    >>> dbf.close()
    """

    encoding = 'GBK'

    def __init__(self):
        self.reader = DbfReader()
        self.data = None
        self.delflag = None

    def open(self, filename: str = ''):
        """
        open and load dbf to self.data

        Args:
            filename(str): dbf file name to read
        """
        self.reader.encoding = self.encoding
        self.reader.open(filename=filename)
        if isinstance(self.reader.data, pd.DataFrame):
            self.__data_cleaning()

    def close(self):
        """
        close dbf file
        fetch is not available after the close method is executed
        """
        self.reader.close()

    def fetch(self, start=1, count=10):
        """
        从DBF文件读出数据到Dbf对象属性data
        开始记录号从1至DBF的最大记录长度
        read DBF file records to Dbf attribute data
        start in range(1, len(dbf)+1)

        Args:
            start(int): start record number to read
            count(int): record count to read
        """
        if start < 0 or count < 0:
            self.reader.fetchall()
        else:
            self.reader.fetchmany(start=start, count=count)
        self.__data_cleaning()

    def to_csv(self, csvfile='temp.csv', sep=',', **kwargs):
        """
        将self.data写入csv文件csvfile

        Args:
            csvfile(str): csv file name to save
            sep(str): seperator used in csv file
            kwargs(dict)； key parameters used for method DataFrame.to_csv
        """
        if not isinstance(self.data, pd.DataFrame):
            raise FileNotFoundError('no data to save to csv!')
        self.data.to_csv(csvfile, index=False, sep=sep, **kwargs)

    def to_dbf(self, dbffile='tempdbf.dbf'):
        if not isinstance(self.data, pd.DataFrame):
            raise FileNotFoundError('no data to save to csv!')
        writer = DbfWriter()
        writer.encoding = self.encoding
        writer.to_dbf(df=self.data, dbffile=dbffile)

    def __data_cleaning(self):
        """
        对象内部数据转换方法方法
        将self.data设置为DBf读出数据self.reader.data的视图，不包含数据列_delflag
        设置self._delflag，作为self.reader.data._delflag数据列视图（Series）

        object internal data conversion method,
        set self.data as a view of self.reader.data
        set self._delflag as a view of self.readerdata[_delflag]
        """
        df = self.reader.data
        self.delflag = df['_delflag'] if '_delflag' in df.columns else None
        self.data = df[[col for col in df.columns if col != '_delflag']]
