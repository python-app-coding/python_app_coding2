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
from .dbfreader import DbfReader


# set to normal 四舍五入 mode
decimal.getcontext().rounding = decimal.ROUND_HALF_UP


class DbfWriter:
    # public parameters
    encoding = 'GBK'
    max_decimal = 4

    # infer 6 types for dbf from DataFrame dtypes
    # other types remained to str
    missing_value_map = OrderedDict(
        N=0,
        C='',
        F=0,
        I=0,
        O=0,
        D='00010101',
        L=False
    )

    __Field_Spec = namedtuple('Field', ['name', 'type', 'size', 'decmial'])

    __type_checker = OrderedDict(
        N=[pd._libs.lib.is_integer_array],
        B=[pd._libs.lib.is_float_array],
        L=[pd._libs.lib.is_bool_array],
        D=[pd._libs.lib.is_date_array],
        T=[pd._libs.lib.is_datetime_array, pd._libs.lib.is_datetime64_array],
        C=[pd._libs.lib.is_string_array],
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
        >>> dbw = DbfWriter()
        >>> dbw.to_dbf(df, 'demo.dbf')

        # read for checking
        >>> dbr = DbfReader()
        >>> dbr.open('demo.dbf')
        >>> dbr.data
           _delflag serial_no       en_name ch_name   price                shipping
        0     False     10101  Refrigerator      冰箱  310.51  b'2020-03-01 01:00:00'
        1     False     10102        Washer     洗衣机  420.35  b'2020-03-02 01:00:00'
        2     False     10103         Stove      炉子  350.00  b'2020-03-03 00:30:00'
        3     False     10104    Ventilator     通风机  210.40  b'2020-03-04 00:00:30'
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
            raise EOFError('Error: cannot create dbf file {}'.format(dbffile))

        # get field info
        self.field_spec = DbfWriter.get_field_spec_from_dataframe(self.df)

        # get data with fields in field_spec
        df = self.df[[fd.name for fd in self.field_spec]]

        # write dbf header
        DbfWriter.write_dbf_header(fp, self.field_spec, df)

        # write dbf records
        DbfWriter.write_dbf_records(fp, self.field_spec, df)

        # write dbf end char
        fp.write(b'\x1A')
        fp.close()

    @staticmethod
    def get_field_spec_from_dataframe(df):
        """
        use some strategies to set field type,size,decimal
        use type for dbf, dtype for DataFrame in following:
        for each column in data(DataFrame.columns)
        0. set type='G', decimal=0 for initial, that means to set any dtypes to G if type_check.keys) return None
        1. set type=_type if DbfWriter.type_check[_type][data.column] is in {N,B,L,D,T,C}
           where need to filter NaN from data.column
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
            for k in DbfWriter.__type_checker.keys():
                for checker in DbfWriter.__type_checker[k]:
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
            field_spec.append(DbfWriter.__Field_Spec(col, field_type, field_size, field_decimal))
        return field_spec

    @staticmethod
    def write_dbf_header(fp, field_spec, data):
        """
        analyze and write header_info (including: file-info, field-inof, terminator, extended 263 bytes)
        1. calculate record_count, field_count from df
        2. set time, version
        3. count field_len, header_len
        4. write file-info
        5. write field-info by encoding and pack self.field_spec
        6. write terminator+263bytes
        :param fp: file handle
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
    def write_dbf_records(fp, field_spec, df):
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
