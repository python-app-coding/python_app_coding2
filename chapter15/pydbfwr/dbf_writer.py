# coding = utf8


# import time
# import io
# import os
import struct
import datetime
from collections import namedtuple
from collections import OrderedDict
import decimal
import numpy as np
import pandas as pd

# set to normal 四舍五入 mode
decimal.getcontext().rounding = decimal.ROUND_HALF_UP


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
        T=[pd._libs.lib.is_datetime_array, pd._libs.lib.is_datetime64_array],
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

