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

    def open(self, filename=None):
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
            raise FileNotFoundError('Error: dbf file [{}] not found!'.format(filename))
        else:
            self.parse_header()
            self.fetchmany(1, 10)
            self.report = 'use {}'.format(filename)
            self.filename = filename

    def fetchall(self):
        st = time.localtime()
        self.runtime = 'read data start: {}-{}-{} {}:{}:{}\n'. \
            format(st.tm_year, st.tm_mon, st.tm_mday, st.tm_hour, st.tm_min, st.tm_sec)
        if not self.file_handle:
            raise FileNotFoundError('Error: no file handle found!')
        st = time.time()
        data_dict = {field.name: [] for field in self.field_info}
        fp = self.file_handle
        fp.seek(self.file_info.header_len)
        for i in range(self.file_info.record_count):
            result = self.parse_record(fp)
            for fi, field in enumerate(self.field_info):
                data_dict[field.name].append(result[fi])
        self.runtime += 'read data from dbf ellapsed={:5.2f}\n'.format(time.time() - st)
        st = time.time()
        self.data = pd.DataFrame(data_dict)
        self.data = self.data.astype(self.field_astype)
        self.runtime += 'set data to pandas ellapsed={:5.2f}'.format(time.time() - st)
        st = time.localtime()
        self.runtime += 'read data end: {}-{}-{} {}:{}:{}\n'. \
            format(st.tm_year, st.tm_mon, st.tm_mday, st.tm_hour, st.tm_min, st.tm_sec)
        self.report += self.runtime

    def fetchmany(self, begin=1, count=10):
        if not self.file_handle:
            raise FileNotFoundError('Error: no file handle found!')
        record_count = self.file_info.record_count
        if begin not in range(1, record_count + 1):
            self.report = 'begin record ={} is not in dbf file!'.format(begin)
            return
        get_record_num = count
        if (begin + count - 1) > record_count:
            get_record_num = record_count - begin + 1
            self.report = 'Warning: record count is beyond bound!'
        data_dict = {field.name: [] for field in self.field_info}
        fp = self.file_handle
        fp.seek(self.file_info.header_len + (begin - 1) * self.file_info.record_len)
        for ri in range(get_record_num):
            result = self.parse_record(fp)
            for fi, field in enumerate(self.field_info):
                data_dict[field.name].append(result[fi])
        self.data = pd.DataFrame(data_dict)

    def parse_header(self):
        fp = self.file_handle

        # read file info
        file_type, year, month, day, record_count, header_len, record_len = \
            struct.unpack('<c3BLHH20x', fp.read(32))
        file_type = str(file_type) + '--' + self.dbf_version.get(file_type, file_type)

        # read field info
        field_delflag_name = '_delflag'
        self.field_info = [self.Record_Spec(field_delflag_name, 'L', 1, 0)]     # add field _delflag
        field_count = 1                                                         # including field _delflag
        for _ in range((header_len-33) // 32):                                  # field_count <= (header_len - 33) // 32
            first_byte = fp.read(1)                                             # avoid to read out of file-data
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

    def parse_record(self, fp):
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

        :param fp: file handle
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
                field_value = get_datetime_from_dbftime(field_value)
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


def get_date_from_epoch_days(date_days):
    """
    get year, month, day from ellapsed days from epoch datetime(1, 1, 1)
    max value of date_days is 3652058, that is datetime(9999, 12, 31) - datetime(1,1,1)

    >>> get_date_from_epoch_days(721906)
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
    if year_no in get_leap_years(year_no, year_no):
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


def get_leap_years(beg, end):
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

    >>> get_leap_years(1, 20)
    [4, 8, 12, 16, 20]
    >>> get_leap_years(-10, -1)
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

    Python-func maybe run slower, C-code should be used in future
    """

    # parse date_value and time_value separately
    _date_days, _time_value = struct.unpack('<ii', dbftime)

    # only support AC date in some range
    # BC date is invalid in dbf and datetime
    if _date_days >= 1721426:
        # valid time range:
        #     time.localtime(v) limits v start from 1970.1.1
        #     datetime range is 1.1.1 0:0:0 - 9999.12.31 59:59:999999
        # time conversion:
        #   _date_time = time.localtime((_date_days-1721426)*24*3600)
        #   _date = _date_time.tm_year, _date_time.tm_mon, _date_time.tm_mday
        _date = get_date_from_epoch_days(_date_days - 1721426)
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
            _time_h = 0
        _time = _time_h, _time_m, _time_s
        return datetime.datetime(*_date, *_time)
