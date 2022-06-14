# coding = utf8


import time
import struct
import datetime
import io
import os
from collections import namedtuple
from collections import OrderedDict
import decimal
import numpy as np
import pandas as pd

# set to normal 四舍五入 mode
decimal.getcontext().rounding = decimal.ROUND_HALF_UP


def read_dbf(dbf: str) -> pd.DataFrame:
    """
    读取dbf文件为DataFrame
    read dbf file

    read_dbf(dbf: str) -> pd.DataFrame
    :param dbf: dbf file name, suffix .dbf is needed
    :return: DataFrame
    """
    dbfobj = Dbf()
    dbfobj.use(dbf)
    dbfobj.load(count=-1)
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
    dbfobj.use()


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
    (Examples)
    >>> dbf = Dbf()
    >>> dbf.use('demo.dbf')
    >>> dbf.load(1, 20)
    >>> dbf.use()
    """

    def __init__(self, encoding='gbk'):
        self.encoding = encoding
        DbfReader.encoding = encoding
        self.reader = DbfReader()
        self.data = None
        self.delflag = None
        self.writer = None

    def set_data(self, df):
        """
        set df to self.data
        filter out the fields in df: _delflag
        :param df: DataFrame to set to self.data
        """
        self.data = df
        self.delflag = self.data['_delflag'] if '_delflag' in self.data.columns else None
        self.data = self.data[[col for col in self.data.columns if col != '_delflag']]

    def use(self, filename: str = ''):
        """
        open and load dbf to self.data
        :param filename:
        :return:
        """
        if os.path.isfile(filename):
            self.reader.use(filename=filename)
            # self.data = self.reader.data[[fd.name for fd in self.reader.field_info
            #                               if not fd.name.startswith('_delflag')]]
            self.set_data(self.reader.data)
        else:
            self.reader.use()
            self.data = None

    def load(self, start=1, count=10):
        if start < 0 or count < 0:
            self.reader.get_all()
        else:
            self.reader.get_some(begin=start, count=count)
        # self.data = self.reader.data
        self.set_data(self.reader.data)

    def to_csv(self, csvfile='temp.csv', sep=','):
        if not isinstance(self.data, pd.DataFrame):
            raise FileNotFoundError('no data to save to csv ch3file!')
        self.data.to_csv(csvfile, index=False, sep=sep)

    def to_dbf(self, dbffile='temp.dbf'):
        if not isinstance(self.data, pd.DataFrame):
            raise FileNotFoundError('no data to save to csv ch3file!')
        DbfWriter.encoding = self.encoding
        self.writer = DbfWriter()
        self.writer.to_dbf(df=self.data, dbffile=dbffile)


class DbfReader:

    dbf_version = {
       b'\x02': 'FoxBASE',
       b'\x03': 'FoxBASE+/dBASE III PLUS，无备注',
       b'0': 'Visual FoxPro',
       b'2': 'Visual FoxPro -9.0',
       b'C': 'dBASE IV SQL 表文件，无备注',
       b'c': 'dBASE IV SQL 系统文件，无备注',
       b'\x83': 'FoxBASE+/dBASE III PLUS，有备注',
       b'\x8b': 'dBASE IV 有备注',
       b'\xcb': 'dBASE IV SQL 表文件，有备注',
       b'\xf5': 'FoxPro 2.x（或更早版本）有备注',
       b'\xfb': 'FoxBASE'
    }
    type_map = {
        'N': float,
        'C': str,
        'D': np.datetime64,
        'L': bool,
        'F': float,
        'I': float
        }
    File_Info = namedtuple(
        'File_Info',
        ('type', 'year', 'month', 'day',
         'record_count', 'header_len',
         'record_len', 'field_count')
        )
    Record_Spec = namedtuple('Record', ('name', 'type', 'size', 'decimal'))
    encoding = 'GBK'

    def __init__(self):
        self.file_handle = None
        self.filename = None
        self.file_info = None
        self.data = None
        self.file_info = None
        self.field_info = []
        self.field_astype = None
        self.field_unpack_format = None
        self.data = None
        self.report = ''
        self.runtime = 0

    def __del__(self):
        if self.file_handle:
            self.file_handle.close()

    def __getitem__(self, item):
        return self.data.loc[item, :]

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(self.file_handle, io.BufferedIOBase):
            self.file_handle.close()

    def use(self, filename=None):
        """
        open dbf and load 10 rows of records to data
        :param filename: dbf file name
        :return: None
        """
        if not filename:
            if isinstance(self.file_handle, io.BufferedReader):
                self.file_handle.close()
            self.file_handle = None
            return
        try:
            self.file_handle = open(filename, 'rb')
        except (FileNotFoundError, IOError) as e:
            self.report = repr(e)
            raise FileNotFoundError('Error: dbf ch3file [{}] could not be opened!'.format(filename))
        else:
            self.read_header()
            self.get_some(1, 10)
            self.report = 'use {}'.format(filename)
            self.filename = filename

    def get_all(self):
        st = time.localtime()
        self.runtime = 'read data start: {}-{}-{} {}:{}:{}\n'.\
            format(st.tm_year, st.tm_mon, st.tm_mday, st.tm_hour, st.tm_min, st.tm_sec)
        if not self.file_handle:
            raise FileNotFoundError('Error: no ch3file handle found!')
        st = time.time()
        data_dict = {field.name: [] for field in self.field_info}
        fp = self.file_handle
        fp.seek(self.file_info.header_len)
        for i in range(self.file_info.record_count):
            result = self.read_record(fp)
            for fi, field in enumerate(self.field_info):
                data_dict[field.name].append(result[fi])
        self.runtime += 'read data from dbf ellapsed={:5.2f}\n'.format(time.time() - st)
        st = time.time()
        self.data = pd.DataFrame(data_dict)
        self.data = self.data.astype(self.field_astype)
        self.runtime += 'set data to pandas ellapsed={:5.2f}'.format(time.time() - st)
        st = time.localtime()
        self.runtime += 'read data end: {}-{}-{} {}:{}:{}\n'.\
            format(st.tm_year, st.tm_mon, st.tm_mday, st.tm_hour, st.tm_min, st.tm_sec)
        self.report += self.runtime

    def get_some(self, begin=1, count=10):
        if not self.file_handle:
            raise FileNotFoundError('Error: no ch3file handle found!')
        record_count = self.file_info.record_count
        if begin not in range(1, record_count + 1):
            self.report = 'begin record ={} is not in dbf ch3file!'.format(begin)
            return
        get_record_num = count
        if (begin + count - 1) > record_count:
            get_record_num = record_count - begin + 1
            self.report = 'Warning: record count is beyond bound!'
        data_dict = {field.name: [] for field in self.field_info}
        fp = self.file_handle
        fp.seek(self.file_info.header_len + (begin - 1) * self.file_info.record_len)
        for ri in range(get_record_num):
            result = self.read_record(fp)
            for fi, field in enumerate(self.field_info):
                data_dict[field.name].append(result[fi])
        self.data = pd.DataFrame(data_dict)

    def read_header(self):
        fp = self.file_handle

        # read ch3file info
        file_type, year, month, day, record_count, header_len, record_len = \
            struct.unpack('<c3BLHH20x', fp.read(32))
        file_type = str(file_type) + '--' + self.dbf_version.get(file_type, file_type)

        # read field info
        field_delflag_name = '_delflag'
        self.field_info = [self.Record_Spec(field_delflag_name, 'L', 1, 0)]     # add field _delflag
        field_count = 1                                                         # including field _delflag
        for _ in range((header_len-33) // 32):                                  # field_count <= (header_len - 33) // 32
            first_byte = fp.read(1)                                             # avoid to read out of ch3file-data
            if first_byte == b'\r':
                break
            # else:
            data = first_byte + fp.read(31)
            # parse name, type, size, decimal
            _record = struct.unpack('<11sc4xBB14x', data)
            _name = _record[0].replace(b'\x00', b'').decode(self.encoding).lower()
            _type = _record[1].decode(self.encoding)
            _record = self.Record_Spec(_name, _type, *_record[2:])
            # no _delflag in dbf
            if _name == field_delflag_name:
                self.field_info[0] = self.Record_Spec('_'+field_delflag_name, 'L', 1, 0)
                # print(_name, field_delflag_name)
            self.field_info.append(_record)
            field_count += 1

        # set file_info, field_parse_format, field_astype
        self.file_info = self.File_Info(file_type, year, month, day, record_count,
                                        header_len, record_len, field_count)
        self.field_unpack_format = ''.join(['{}s'.format(fd.size) for fd in self.field_info])
        self.field_astype = {fd.name: self.type_map.get(fd.type, str)
                             for fd in self.field_info}

    def read_record(self, fp):
        """
        convert data from dBase types to pandas types:
            dBase  type: C, V, N, F, D, L, I, B, O, T, @
            pandas type: str, int64, decimal.Decimal, np.date, datetime, bool, np.float64

        parse dbf data to pandas:
            C, V: decode to str by bytes.decode
            N, F: decode to str by bytes.decode
                  parse to Decimal if decimal > 0 else to int
               I: decode to integer by unpack
               D: decode to str by bytes.decode
                  parse date by datetime.date(year, month, day)
            T, @: decode to datetime by unpack 2 long integers
                  parse to date and time by get_date_by_days and get_time_by_compound_value
            B, O: decode to float64 by unpack
               L: decode to str by bytes.decode
                  parse to True if 'YyTt' else False
           other: remain to binary byte string, including(G,P,M,Y,...)

        :param fp: ch3file handle
        :return: list with field-data
        """
        _record = struct.unpack(self.field_unpack_format,
                                fp.read(self.file_info.record_len))
        result = []
        # for ri in range(self.file_info.field_count):
        for ri, field_value in enumerate(_record):
            # get field-info
            _name = self.field_info[ri].name
            _type = self.field_info[ri].type
            _decimal = self.field_info[ri].decimal
            _size = self.field_info[ri].size

            # parsing-1: decode field_value to str for 'N,F,D,C,V'
            if _type in 'N,F,D,C,V':
                field_value = field_value.replace(b'\x00', b'').decode(self.encoding).strip()

            # parsing-2: convert field_value according to its type
            if _type in "N,F":
                # N, F: numeric type, float, fixed-point, digital char
                # set to Decimal if _decimal > 0
                if _decimal:
                    field_value = decimal.Decimal(field_value)
                else:
                    field_value = int(field_value) if field_value.isdigit() else None
            elif _type == 'I':
                # I: integer type in dBase, 4 bytes, signed
                field_value = struct.unpack('<i', field_value)[0]
            elif _type in 'B, O':
                # B, O: double type in dBase, 8 bytes
                field_value = struct.unpack('<d', field_value)[0]
            elif _type == 'D':
                # D: date, str, format='YYYYMMDD'
                if field_value.replace('0', '') == '':
                    field_value = None
                else:
                    _date = int(field_value[:4]), int(field_value[4:6]), int(field_value[6:8])
                    field_value = None if not all(_date) else datetime.date(*_date)
            elif _type == 'L':
                if _name == '_delflag':
                    # get delflag to set field _delflag
                    field_value = False if field_value == b'\x20' else True
                else:
                    # set to False for uninitialized value '?'
                    field_value = field_value in b'YyTt?'
            elif _type in 'T, @':
                # consume much time to process
                field_value = DbfReader.get_datetime_from_dbftime(field_value)
            # elif _type in 'C,V':
            #     # remain str
            #     pass
            # else:
                # remain as binary string for type[Y, M, G, P]
                # Y: money format
                # M: comments pointer
                # G: general binary format
                # P: picture data

            # set value to result
            result.append(field_value)
        return result

    @staticmethod
    def get_date_from_days(date_days):
        """
        get year, month, day from ellapsed days
        max value of date_days is 3652058, that is datetime(9999, 12, 31) - datetime(1,1,1)
        >>> DbfReader().get_date_from_days(721906)
        (1977, 7, 7)
        """
        month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # set upper value of year to max year in datetime
        year_max, year_min = 9999, 1
        # year_no = 0     # initialize to 0, raise exception if not found in searching
        while True:
            year_mean = int((year_max+year_min)/2)
            diff = (datetime.datetime(year_mean, 1, 1) - datetime.datetime(1, 1, 1)).days
            if diff > date_days:
                year_max = year_mean
            else:
                year_min = year_mean
            if (year_max - year_min) <= 1:
                year_no = year_min
                break
        else_days = date_days - (datetime.datetime(year_no, 1, 1) - datetime.datetime(1, 1, 1)).days
        # set leap_year month_day
        if year_no in DbfReader.get_leap_year(year_no, year_no):
            month_day[1] = 29
        year_days = sum(month_day)
        if else_days >= year_days:
            year_no += 1
            else_days -= year_days
        # find month no by cumulate month_days util sum>else_days
        month_no = 1
        for i, m in enumerate(month_day):
            if sum(month_day[:i+1]) > else_days:
                month_no = i + 1
                break
        # set remain days to day_no
        day_no = else_days - sum(month_day[:month_no-1]) + 1
        return year_no, month_no, day_no

    @staticmethod
    def get_leap_year(beg, end):
        """
        calculate leap years from begin year(beg) to end year(end)
        based on principle:
        leap year merges for every 4 years
        the year with year//100 == year is not leap year
        the year with year//400 == year is a leap year
        leap year with 366 days, other years with 365

        计算从 beg 到 end 之间的闰年
        基于的原则：4年一闰，100年不闰，400年闰
        公元前年份：除4余数1的年份闰，除100余1的年份不闰，除400余1的年份闰
        闰年366天，平年365天
        :param beg: 开始年
        :param end: 结束年
        :return: 闰年年份的列表
        >>> DbfReader.get_leap_year(1, 20)
        [4, 8, 12, 16, 20]
        >>> DbfReader.get_leap_year(-10, -1)
        [-9, -5, -1]
        """
        beg = 1 if not beg else beg
        end = datetime.datetime.now().year if not end else end
        if end < beg:
            raise ValueError('end-year={} < beg-year={}'.format(end, beg))
        leap = []
        for y in range(beg, end + 1):
            if y == 0:
                continue
            if y > -100:
                _y = y - 3 if y < 0 else y
            else:
                _y = y + 1 if y < 0 else y
            if ((_y % 100) and (_y % 4 == 0)) | (_y % 400 == 0):
                leap.append(y)
        return leap

    @staticmethod
    def get_datetime_from_dbftime(dbftime):
        """
        valid year range returned: 1-9999
        date valid value in dBase: year 0001-9999, hour 00-23, minute 00-59, second 00-59
        dBasetime = date_value(integer) + time_value(integer)
        parse datetime.date from date_value:
          the value of year in dBase is the days, that is ellapsed days from BC 4713 (not confirmed!)
          1721426 days is the days from date(1-1-1) to some BC time point(4712.11.22) defined in dBase
          for any date x, there si an equation:
            dbase.time.year(days) - 1721426 == (x - datetime(1,1,1)).days
            set x in DataFrame
            get dBase.days from the equation
        parse datetime.time from time_value:
          dBase-time-value: hour*3600000 + minute*60000 + seconds*1000
          time_hour = time_value // 3600000
          time_min  = (time_value - time_hour*3600000) // 60000
          time_sec  = (time_value - time_hour*3600000 - time_min*60000 + 1) // 1000
          Note: the value in dBasetime is real value minus 1, that is verified by comparing real value
        """

        # parse date_value and time_value separately
        _date_days, _time_value = struct.unpack('<ii', dbftime)

        # only support AC date: BC date is invalid in dbf and datetime
        if _date_days >= 1721426:
            # module-time can not be used,
            # because of time.localtime(v) limits v start from 1970.1.1
            #            datetime range is 1.1.1 0:0:0 - 9999.12.31 59:59:999999
            # module-time code:
            #   _date_time = time.localtime((_date_days-1721426)*24*3600)
            #   _date = _date_time.tm_year, _date_time.tm_mon, _date_time.tm_mday
            # python-func maybe run slower, C-extend code should be used in future
            _date = DbfReader.get_date_from_days(_date_days - 1721426)
            _time_h = _time_value // 3600000
            _time_m = (_time_value - _time_h * 3600000) // 60000
            _time_s = (_time_value - _time_h * 3600000 - _time_m * 60000 + 1) // 1000
            if _time_s >= 60:
                _time_s = 0
                _time_m += 1
            if _time_m >= 60:
                _time_m = 0
                _time_h += 1
            if _time_h >= 24:
                print(_time_h)
                _time_h = 0
            _time = _time_h, _time_m, _time_s
            # print(_date, _time)
            return datetime.datetime(*_date, *_time)
        else:
            return None


class DbfWriter:
    # public parameters
    encoding = 'GBK'
    max_decimal = 4

    # interior parameters
    # check out 6 types from pandas used to write data to dBase
    # other types remained to parse furtherly, for example, decimal.Decimal
    _type_checker = OrderedDict(
        N=[pd._libs.lib.is_integer_array],
        B=[pd._libs.lib.is_float_array],
        L=[pd._libs.lib.is_bool_array],
        D=[pd._libs.lib.is_date_array],
        T=[pd._libs.lib.is_datetime_array, pd._lib.is_datetime64_array],
        C=[pd._libs.lib.is_string_array],
        )
    _Field_Spec = namedtuple('Field', ['name', 'type', 'size', 'decmial'])
    _missing_value_map = OrderedDict(
        N=0,
        C='',
        F=0,
        I=0,
        O=0,
        D='00010101',
        L=False
        )

    def __init__(self):
        self.df = None
        self.field_spec = None
        self.report = ''

    def to_dbf(self, df, dbffile='tempdbf.dbf'):
        """
        covert DataFrame to dBase file

        procedure:
        1. get field_spec for dBase from DataFrame columns dtype
        2. write dbf header using DataFrame.len, field_spec
        3. write dbf records according to DataFrame.row and field_spec
           write delflag of dBase record to b' ' or b'\2a' when DataFrame._delflag is False or True

        field_spec, list with item: namedtuple(name, type, size, decimal)
           name:strlen(name)<=11,
           type must in 'C N F I O D L'
           size:int=len(field),
           decimal:int

        Notes:
            before use to_dbf, can set DbfWriter.max_decimal, DbfWriter.codeset

        example:
        >>> import pandas as pd
        >>> from datetime import datetime as dt
        >>> df = pd.DataFrame({'serial_no': ['10101', '10102', '10103', '10104'],\
                               'en_name': ['Refrigerator', 'Washer', 'Stove', 'Ventilator'], \
                               'ch_name': ['冰箱', '洗衣机', '炉子', '通风机'], \
                               'price': [310.51, 420.35, 350, 210.4],\
                               'shipping': [dt(2020, 3, 1, 1, 0, 0), dt(2020, 3, 2, 1, 0, 0), \
                                            dt(2020, 3, 3, 0, 30, 0), dt(2020, 3, 4, 0, 0, 30)]\
                               })
        >>> DbfWriter.encoding = 'gbk'
        >>> dbw = DbfWriter()
        >>> dbw.to_dbf(df, 'demo.dbf')
        >>> dbr = DbfReader()
        >>> dbr.use('demo.dbf')
        >>> dbr.data['serial_no'][0:2]
        0    10101
        1    10102
        Name: serial_no, dtype: object
        """
        self.report = ''

        # check df
        if not isinstance(df, pd.DataFrame):
            raise ValueError('df is not DataFrame!')
        else:
            self.df = df
        if len(self.df) == 0:
            raise ValueError('Warning: data is empty!')

        # open dbf
        try:
            fp = open(dbffile, 'wb')
        except EOFError:
            raise EOFError('Error: cannot create dbf ch3file {}'.format(dbffile))

        # get field info
        self.field_spec = DbfWriter.get_field_spec(self.df)

        # get data with fields in field_spec
        df = self.df[[fd.name for fd in self.field_spec]]

        # write dbf header
        DbfWriter.write_header(fp, self.field_spec, df)

        # write dbf records
        DbfWriter.write_records(fp, self.field_spec, df)

        # write dbf end char
        fp.write(b'\x1A')
        fp.close()

    @staticmethod
    def get_field_spec(df):
        """
        use some strategies to set field type,size,decimal
        for each column in data(DataFrame.columns)
        0. set type='G', decimal=0 for initialization, mean to set other types to G (not in type_check.keys)
        1. set type=_type if DbfWriter.type_check[_type][data.column], that is in {N,B,L,D,T,C}
           where need to filter None/NaN from data.column
        2. set len=8 for type(D, T)
        3. set len=4, type='I' if range(-2**32, 2**32) for type(N)
           set len=maxlen if abs >= 2**32 for type(N)
        4. set len=8 for type(B), double-float
        5. set len=1 for type(L)
        6. for type(Decimal) by pandas._libs_lib.is_decimal(data.column):
               get max_int_len, max_decimal_len from DataFrame
               if max_decimal_len too large, set to default len: DbfWriter.max_decimal
               set type='N', size=max_int_len+max_decimal_len+1 for type(Decimal)
           set len=max_str_encode_len for type(G)

        :param df: pandas.DataFrame
        :return: dbf field specification [(name, type, size, decimal), ...]
        """
        field_spec = []
        for col in df.columns:
            if col == '_nullflags':
                continue
            field_type = 'G'
            field_decimal = 0
            data = np.array(df.loc[df[col].notna(), col])
            # type D < T, checked type-datetime after type-date
            for k in DbfWriter._type_checker.keys():
                for checker in DbfWriter._type_checker[k]:
                    if checker(data):
                        # print('field={} type={}'.format(col, k))
                        field_type = k
            # check type and size
            if field_type in 'D,T':
                field_size = 8
            elif field_type == 'N':
                if -2 ** 31 < max(df[col]) < 2 ** 31:
                    field_type = 'I'
                    field_size = 4
                else:
                    field_size = max(df[col].apply(str))
            elif field_type == 'B':
                field_size = 8
            elif field_type == 'L':
                field_size = 1
            else:
                # check Decimal type, size to fixed type(N, size, decimal)
                data = df.loc[df[col].notna(), col]
                if all([pd._libs.lib.is_decimal(x) for x in data]):
                    field_int_len = max(data.apply(lambda x: len(str(int(x)))))
                    field_decimal = max(data.apply(lambda x: 0 if x-int(x) == 0 else len(str(x-int(x)))-2))
                    if field_decimal > DbfWriter.max_decimal:
                        field_decimal = DbfWriter.max_decimal
                    field_size = field_int_len + field_decimal + 1
                    field_type = 'N'
                else:  # C, G
                    field_size = max(df[col].apply(lambda x: len(str(x).encode('gbk'))))
            field_spec.append(DbfWriter._Field_Spec(col, field_type, field_size, field_decimal))
        return field_spec

    @staticmethod
    def write_header(fp, field_spec, data):
        """
        analyze and write header_info (including: file-info, field-inof, terminator, extended 263 bytes)
        1. calculate record_count, field_count from df
        2. set time, version
        3. count field_len, header_len
        4. write ch3file-info
        5. write field-info by encoding and pack self.field_spec
        6. write terminator+263bytes
        :param fp: ch3file handle
        :param field_spec: field specification, list with items(name, size, type, decimal)
        :param data: data(DataFrame) to write
        """
        # write header
        version = 0x30
        update_time = datetime.datetime.now()
        year, month, day = update_time.year - 1900, update_time.month, update_time.day
        record_count = len(data)
        field_count = len(field_spec)                              # include all columns of data
        header_len = 32 + field_count * 32 + 1 + 263
        record_len = sum(field.size for field in field_spec) + 1   # include all columns of data, and del flag
        header_file_info = struct.pack('<BBBBLHH20x',
                                       version, year, month, day, record_count, header_len, record_len)
        fp.write(header_file_info)
        # write header-field-info without _delflag
        header_field_info = b''
        for _name, _type, _size, _decimal in field_spec:
            value = (_name.encode(DbfWriter.encoding).ljust(11, b'\x00'),
                     _type.encode(DbfWriter.encoding),
                     _size,
                     _decimal)
            header_field_info += struct.pack('<11sc4xBB14x', *value)
        fp.write(header_field_info)
        # write terminator and 263 extended bytes
        fp.write(b'\r' + b'\x00'*263)

    @staticmethod
    def write_records(fp, field_spec, df):
        del_flag = b' '
        # write records
        for row_index, record in df.iterrows():
            # set delflag
            # del_flag = b'\x2A' if ('_delflag' in df.columns) and (record['_delflag']) else b' '
            fp.write(del_flag)

            # encode and write fields
            for (_name, _type, _size, _decimal), value in zip(field_spec, record):
                # process missing value, value in [None, np.NaN]:
                if pd.isna(value):
                    # need to consider further
                    if _type in 'N,D':
                        value = b'0' * _size
                    elif _type in 'C':
                        value = b' '*_size
                    elif _type == 'L':
                        value = b'F'
                    else:
                        value = b'\x00' * _size
                elif _type == 'N':
                    # value = format(value, 'size-decimal-1.decimal').rjust(_size)
                    fmt = str(_size - _decimal - 1) + '.' + str(_decimal) + 'f'
                    value = format(value, fmt)
                    value = value[-_size:] if len(value) > _size else value.rjust(_size)
                    value = value.encode(DbfWriter.encoding)
                elif _type == 'I':
                    value = struct.pack('<i', value)
                elif _type == 'D':
                    # format to 'YYYYmmdd' with '0' filled
                    value = (value.year, value.month, value.day)
                    value = (int(v) if v is not np.NaN else 0 for v in value)
                    value = '{:04d}{:02d}{:02d}'.format(*value).encode(DbfWriter.encoding)
                elif _type == 'T':
                    # use sign integer for 0-1
                    value = datetime.datetime(value.year, value.month, value.day,
                                              value.hour, value.minute, value.second)
                    value_date = (value - datetime.datetime(1, 1, 1)).days + 1721426
                    value_time = value.hour * 3600000 + value.minute * 60000 + value.second * 1000
                    value_time = value_time - 1 if value_time > 0 else 100      # 0-999 => 0 for seconds
                    value = struct.pack('<ii', value_date, value_time)
                elif _type == 'L':
                    # bool type
                    value = b'T' if value else b'F'
                elif _type == 'C':
                    value = value.encode(DbfWriter.encoding)
                    value = value + b' ' * (_size - len(value))
                elif _type in 'B':
                    value = struct.pack('<d', value)
                else:
                    value = str(value)
                    value_encode = value.encode(DbfWriter.encoding)
                    while len(value_encode) > _size:
                        value = value[:-1]
                        value_encode = value.encode(DbfWriter.encoding)
                    len_diff = _size - len(value_encode)
                    value = value_encode + b'\x00' * len_diff
                fp.write(value)

    def get_dbf_type(self):
        df = self.df
        report = ''
        columns = [col for col in df if col not in ['_nullflags']]
        data = df[columns]
        field_info = []
        for col in columns:
            _name = col
            _size = 8
            _decimal = 0
            pandas_type = str(type(data[col][0]))
            # print(pandas_type)
            if 'bool' in pandas_type:
                _type = 'L'
                _size = 1
            elif ('Decimal' in pandas_type) or ('float' in pandas_type):
                _type = 'B'     # Foxpro=B, O maybe in dBase IV
            elif 'int' in pandas_type:
                _max = max(data[col])
                _min = min(data[col])
                if _max < 2**32 and _min > -2**32:
                    _type = 'I'
                    _size = 4
                else:
                    _type = 'N'
                    _size = len(str(_max)) + (1 if _min < 0 else 0)
            elif 'datetime.datetime' in pandas_type:
                _type = 'T'
            elif 'datetime.date' in pandas_type:
                _type = 'D'
            elif 'str' in pandas_type:
                _type = 'C'
                _size = max(data[col].apply(lambda x: len(x.encode(self.encoding))))
            else:
                _type = 'G'
                _size = max(data[col].apply(str).apply(len))
            report += 'info: set field {} type to {}\n'.format(col, _type)
            field_info.append(DbfWriter._Field_Spec(_name, _type, _size, _decimal))
        self.field_spec = field_info
        self.report = report

    def reset_field_info(self, field_info):
        """
        set field_info
        need to match dataframe to write to dbf
        :param field_info: [(name, type, size, decimal), ...]
        :return: None
        set field_into to self.field_info, write self.report
        """
        self.report = ''
        columns = []
        for fd in field_info:
            if fd[0] in self.df.columns:
                columns.append(fd[0])
            else:
                self.report += 'Warning: field name {} not in data.columns!\n'.format(fd[0])
        field_info = [fd for fd in field_info if fd[0] in columns]
        # check field type compatibility
        # set to type-G if conflict found
        # set to type-G if not in 'NFODLCV'(donnt support else data-type)
        for j, fd in enumerate(field_info):
            type_str = str(type(self.df[fd[0]][0]))
            if (fd[1] in 'N, F, O' and 'float' not in type_str) or \
                    (fd[1] == 'D' and 'date' not in type_str) or \
                    (fd[1] == 'L' and 'bool' not in type_str) or \
                    (fd[1] in 'C, V' and 'str' not in type_str) or \
                    fd[1] not in 'NFODLCV':
                field_info[j][1] = 'G'
        self.field_spec = field_info


dbf_doc = \
    """
    DBF ch3file structure description

    DBF表文件由表头区及数据记录区组成。表头定义表结构及表的其他信息。
    DBF表头区从位置0开始。数据记录区紧接在头记录之后（连续的字节）。
    DBF数据记录长度（以字节为单位）等于所有字段定义长度之和。
    DBF表中存储整数时低位字节在前（小端存储）。

    1．DBF表头结构
        字节偏移 说明
        -------------------------------------------------------------------------------------------
        0  文件类型
            0x02    FoxBASE
            0x03    FoxBASE+/dBASE III PLUS，无备注
            0x30    Visual FoxPro
            0x43    dBASE IV SQL 表文件，无备注
            0x63    dBASE IV SQL 系统文件，无备注
            0x83    FoxBASE+/dBASE III PLUS，有备注
            0x8B    dBASE IV 有备注
            0xCB    dBASE IV SQL 表文件，有备注
            0xF5    FoxPro 2.x（或更早版本）有备注
            0xFB    FoxBASE
        1 - 3 最近一次更新的时间（YYMMDD）
        4 - 7 文件中的记录数目
        8 - 9 第一个数据记录的位置（数据区开始位置）
        10 - 11 每个数据记录的长度（包括带有删除标记的记录在内）
        12 - 27 保留
        28 表的标记
            0x01 文件具有.cdx 索引。
            0x02 文件包含备注。
            0x04 文件是数据库（.dbc）
            该字节可以为任何上面值的和： 0x03, 0x05, 0x06, 0x07。
            表示多项同时存在。
            例如，0x03 表明表具有结构化.cdx和一个备注字段。
        29 代码页标记
        30 - 31 保留，包含 0x00
        32 - n 字段子记录
            字段的数目决定了字段子记录的数目。表中每个字段都对应一个字段子记录。
            field_number = (n - 32) // 32
        n+1 头记录终止符（0x0D）
        n+2 到 n+264
            此范围内的 263 个字节包含后链信息（相关数据库 (.dbc) 的相对路径）。
            如果第一个字节为 0x00，则该文件不与数据库关联。因此数据库文件本身总是包含 0x00。
        关于记录的删除记:
            每个记录数据包括：删除标记（1个字节），各字段数据（按照定义中的宽度）
            如果删除标记字节为空格 (0x20)，该记录为未置删除标记，
            如果删除标记字节为星号 (0x2A), 该记录为设置了删除标记。
        -------------------------------------------------------------------------------------------

    2．字段定义结构
        字节偏移 说明
        -------------------------------------------------------------------------------------------
        0 - 10 字段名（最多 10 个字符 -若少于 10 则用空字符 (0x00) 填充）
        11 字段类型
            C-字符型
            Y-货币型
            N-数值型
            F-浮点型
            D-日期型
            T-日期时间型
            B-双精度型
            I-整型
            L-逻辑型
            M-备注型
            G-通用型
            C-字符型（二进制）
            M-备注型（二进制）
            P-图片型
        12 - 15 记录中该字段的偏移量
        16 字段长度（以字节为单位）
        17 小数位数
        18 字段标记
            0x01 系统列（用户不可见）
            0x02 可存储 null 值的列
            0x04 二进制列（只适于字符型和备注型）
        19 - 32 保留
        -------------------------------------------------------------------------------------------

    格式保存的文件标头：
        支持 null 值
        日期时间型、货币型及双精度型数据
        字符字段和备注字段标记为二进制
        在数据库 (.dbc) 文件中添加表

    关于字段数的计算公式:
        Visual Foxpro 版本为表头区增加了263个预留后缀字节
        可以使用下面的公式求出表文件中的字段数：(hlen - 296)/32
        hlen：第一个记录的位置（表头记录的第 8 到第 9 个字节）
        296： 263（表头区后缀信息）+ 1（字段记录终止符）+ 32（文件开始的文件结构记录）
        32：  字段结构记录的长度。
        而对Foxbase或DbaseIII，则可以使用：(hlen-33)//32
        由于各个版本的差异，如无具体测试，仍应使用从33开始的搜索计算字段数
    """
