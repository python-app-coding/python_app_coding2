# coding = utf8

import os
import sys
import pandas as pd

curpath = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, curpath)
from dbfreader import DbfReader
from dbfwriter import DbfWriter


def read_dbf(dbf: str) -> pd.DataFrame:
    """
    读取dbf文件为DataFrame
    read dbf_bak file to DataFrame

    read_dbf(dbf_bak: str) -> pd.DataFrame
    :param dbf: dbf_bak file name, suffix .dbf_bak is needed
    :return: DataFrame
    """
    if not os.path.isfile(dbf):
        raise FileNotFoundError
    dbfobj = Dbf()
    dbfobj.open(dbf)
    dbfobj.fetch(count=-1)
    dbfobj.close()
    return dbfobj.data


def write_dbf(df: pd.DataFrame, dbf: str):
    """
    将DataFrame数据写为DBF文件。
    write DataFrame to DBF file.

    to_dbf(df: pd.DataFrame, dbf_bak: str)
    :param df: 类型为pandas.DataFrame。写入DBF文件的数据。
    :param dbf: 字符串。写入DBF文件的文件名。
    """
    dbfobj = Dbf()
    dbfobj.data = df
    dbfobj.to_dbf(dbf)
    dbfobj.close()


class Dbf:
    """
    ---------------------------------------------------------------------------------------------------------------
    class Dbf()
    读写DBF文件的用户服务类
    A class used to read and write DBF file，its property data is DataFrame。

    属性
    data：DataFrame。用于存放读入的DBF文件数据。

    对象方法
    （object methods）

    open(self, filename: str = '')
        打开一个DBF文件。用于在方法fetch中读入数据，必须在fetch之前打开。
        open a DBF file, prework for load method
        参数
        :parameters
        filename: str, file name to open

    关闭打开的DBF文件。当不需要读取DBF文件数据时，可以关闭打开的DBF文件。
    关闭之后，不能使用fetch方法获取数据
    close()

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

    to_dbf(self, dbffile='temp.dbf_bak')
        将数据写入DBF文件
        write data to DBF file

        :parameters
        dbffile: str. 'temp.dbf_bak'( default). file name to write.

    ---------------------------------------------------------------------------------------------------------------
    读写DBF文件数据过程说明
    (read or write dbase file to or from pandas.DataFrame)
    目前支持的DBF数据类型：C(字符)、N（数值）、F（浮点）、D（日期）、L（逻辑）、T（时间日期）、B（双精度）

    调用方式（call procedure）：
    1. 初始化：          dbf_bak = Dbf()                                 # 创建类Dbf的对象实例
    2. 打开DBF文件：     dbf_bak.open(filename)                           # 打开DBF文件
    3. 读入数据：        dbf_bak.fetch()                                  # 读入DBF文件中的数据
    4. 访问数据          dbf_bak.data                                    # 数据存储在属性变量data，格式为 DataFrame
    5. 写数据csv：       dbf_bak.to_csv(csvname=csvfile，sep=',')        # 将data写到文件csvfile,格式为 csv, 分隔符为sep
    6. 写数据dfb：       dbf_bak.to_dbf(dbfname=dbffile)                 # 将data写到DBF文件

    ---------------------------------------------------------------------------------------------------------------
    数据与接口说明
    (comments for some attributes or interface)
    1. Dbf.data：从DBF文件读入的数据，格式为pandas.DataFrame ( read data to Dbf.data from dbase file)
    2. 从 DBF文件到DataFrame的数据类型转换使用Dbf.type_map，在初始化之前可以查看替换，须保证能够进行类型映射
    3. 对 DBF文件字符内容的解码使用 Dbf.codeset，缺省值为 GBK，初始化之前可以替换
    4. 打开 DBF文件后，可以通过 dbf_bak.file_info查看文件结构信息，通过field_info查看字段结构信息
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
    ----------------------
    标记处理
    （flag field for delete and null flag）
    1. 在从dbf读出数据时，将删除标记读入为一个字段_delflag, 忽略_nullflag
    2. 在向dbf写入数据时，忽略_delflag字段，不写删除标记（所有记录标记 b' '），所有记录标记为未删除

    ---------------------------------------------------------------------------------------------------------------

    调用示例：
    Examples:
    # read dbf to DataFrame
    >>> dbf_bak = Dbf()
    >>> dbf_bak.open('demo.dbf')
    >>> dbf_bak.fetch(1, 20)
    >>> print(dbf_bak.data)
          serial_no       en_name ch_name   price            shipping
    0     10101  Refrigerator      冰箱  310.51 2020-03-01 01:00:00
    1     10102        Washer     洗衣机  420.35 2020-03-02 01:00:00
    2     10103         Stove      炉子  350.00 2020-03-03 00:30:00
    3     10104    Ventilator     通风机  210.40 2020-03-04 00:00:30

    >>> dbf_bak.close()
    """

    encoding = 'GBK'

    def __init__(self):
        self.reader = DbfReader()
        self.data = None
        self.delflag = None

    def open(self, filename: str = ''):
        """
        open and load dbf_bak to self.data
        :param filename: dbf_bak file name to read
        """
        self.reader.encoding = self.encoding
        self.reader.open(filename=filename)
        if self.reader:
            self.__data_cleaning(self.reader.data)

    def close(self):
        """
        close dbf_bak file opened in self.reader
        can not fetch data if reader closed
        """
        self.reader.close()

    def fetch(self, start=1, count=10):
        """
        start in range(1, len(dbf_bak)+1)
        """
        if start < 0 or count < 0:
            self.reader.fetchall()
        else:
            self.reader.fetchmany(start=start, count=count)
        self.__data_cleaning(self.reader.data)

    def to_csv(self, csvfile='temp.csv', sep=',', **kwargs):
        if not isinstance(self.data, pd.DataFrame):
            raise FileNotFoundError('no data to save to csv!')
        self.data.to_csv(csvfile, index=False, sep=sep, **kwargs)

    def to_dbf(self, dbffile='tempdbf.dbf'):
        if not isinstance(self.data, pd.DataFrame):
            raise FileNotFoundError('no data to save to csv!')
        writer = DbfWriter()
        writer.encoding = self.encoding
        writer.to_dbf(df=self.data, dbffile=dbffile)

    def __data_cleaning(self, df):
        """
        fetch df to self.data from self.reader.data
        filter out the fields _delflag in reader.data
        save delflag in self._delflag
        :param df: DataFrame to set to self.data
        """
        self.data = df[[col for col in df.columns if col != '_delflag']]
        self.delflag = df[['_delflag']] if '_delflag' in df.columns else None
