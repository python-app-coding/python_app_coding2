# coding = utf8

import os
import pandas as pd
from .dbf_reader import DbfReader
from .dbf_writer import DbfWriter


def read_dbf(dbf: str) -> pd.DataFrame:
    """
    读取dbf文件为DataFrame
    read dbf file to DataFrame

    read_dbf(dbf: str) -> pd.DataFrame
    :param dbf: dbf file name, suffix .dbf is needed
    :return: DataFrame
    """
    if not os.path.isfile(dbf):
        raise FileNotFoundError
    dbfobj = Dbf()
    dbfobj.open(dbf)
    dbfobj.fetchmany(count=-1)
    return dbfobj.data


def to_dbf(df: pd.DataFrame, dbf: str):
    """
    将DataFrame数据写为DBF文件。
    write DataFrame to DBF file.

    to_dbf(df: pd.DataFrame, dbf: str)
    :param df: 类型为pandas.DataFrame。写入DBF文件的数据。
    :param dbf: 字符串。写入DBF文件的文件名。
    """
    dbfobj = Dbf()
    dbfobj.data = df
    dbfobj.to_dbf(dbf)
    dbfobj.open()


class Dbf:
    """
    ---------------------------------------------------------------------------------------------------------------
    class Dbf(encoding='utf8')

    A class used to read and write DBF file，its property data is DataFrame。

    属性
    data：DataFrame。用于存放读入的DBF文件数据。

    对象方法
    （object methods）

    打开一个DBF文件。用于在方法load中读入数据，必须在load之前打开。
    use(self, filename: str = '')
        open a DBF file, prework for load method
        参数
        :parameters
        filename: str, file name to open

    读入在use方法中打开的DBF文件的数据，存入属性data之中。
    load(self, start=1, count=10)
        read DBF file data from the file opened in use

        :parameters
        start: int, positive, start record serial number to read from DBF file
        count: int, positive, record count to read from DBF file

    将数据写入csv文件
    to_csv(self, csvfile='temp.csv', sep=',')
        write data to csv file

        :parameters
        csvfile: str. 'temp.csv'( default). file name to write.
        sep: str. ','( default).  length is 1. charater used to seperate field data in record line.

    将数据写入DBF文件
    to_dbf(self, dbffile='temp.dbf')
        write data to DBF file

        :parameters
        dbffile: str. 'temp.dbf'( default). file name to write.

    ---------------------------------------------------------------------------------------------------------------
    读写DBF文件数据过程说明
    (read or write dbase file to or from pandas.DataFrame)
    目前支持的DBF数据类型：C(字符)、N（数值）、F（浮点）、D（日期）、L（逻辑）、T（时间日期）、B（双精度）

    调用方式（call procedure）：
    1. 初始化：          dbf = Dbf()                                 # 创建类Dbf的对象实例
    2. 打开DBF文件：     dbf.use(filename)                           # 打开DBF文件
    3. 读入数据：        dbf.load()                                  # 读入DBF文件中的数据
    4. 访问数据          dbf.data                                    # 数据存储在属性变量data，格式为 DataFrame
    5. 切片数据:         dbf[start:end:skip]                         # 按照记录进行切片访问，记录号为 0 ~ record_count-1
    6. 写数据csv：       dbf.to_csv(csvname=csvfile，sep=',')        # 将数据写到文件csvfile,格式为 csv, 分隔符为sep
    6. 写数据dfb：       dbf.to_dbf(dbfname=dbffile)                 # 将数据写到DBF文件

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
    ----------------------
    标记处理
    （flag field for delete and null flag）
    1. 在从dbf读出数据时，忽略删除标记，不显示_delflag, _nullflag
    2. 在向dbf写入数据时，忽略_delflag字段，不写删除标记（所有记录标记 b' '），即删除标记为未删除

    ---------------------------------------------------------------------------------------------------------------

    调用示例：
    Examples:
    >>> dbf = Dbf()
    >>> dbf.open('demo.dbf')
    >>> dbf.fetchmany(1, 20)
    >>> print(dbf.data)
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
        # self.delflag = None

    def open(self, filename: str = ''):
        """
        open and load dbf to self.data
        :param filename:
        :return:
        """
        self.reader.encoding = self.encoding
        self.reader.open(filename=filename)
        if self.reader:
            self.__data_cleaning(self.reader.data)

    def close(self):
        self.data = None
        self.reader = None

    def fetchmany(self, start=1, count=10):
        if start < 0 or count < 0:
            self.reader.fetchall()
        else:
            self.reader.fetchmany(begin=start, count=count)
        self.__data_cleaning(self.reader.data)

    def to_csv(self, csvfile='temp.csv', sep=','):
        if not isinstance(self.data, pd.DataFrame):
            raise FileNotFoundError('no data to save to csv!')
        self.data.to_csv(csvfile, index=False, sep=sep)

    def to_dbf(self, dbffile='temp.dbf'):
        if not isinstance(self.data, pd.DataFrame):
            raise FileNotFoundError('no data to save to csv!')
        # DbfWriter.encoding = self.encoding
        writer = DbfWriter()
        writer.encoding = self.encoding
        writer.to_dbf(df=self.data, dbffile=dbffile)

    def __data_cleaning(self, df):
        """
        set df to self.data
        filter out the fields in df: _delflag
        :param df: DataFrame to set to self.data
        """
        self.data = df
        self.data = self.data[[col for col in self.data.columns if col != '_delflag']]
        # self.delflag = self.reader.data[['_delflag']] if '_delflag' in self.reader.data.columns else None
