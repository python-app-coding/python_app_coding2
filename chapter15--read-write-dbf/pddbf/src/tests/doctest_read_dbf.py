# coding: utf8

# import os
import struct
from collections import namedtuple
import decimal
import datetime


file_type_dict = {
    '0x20': "Foxbase",
    '0x03': "FoxBASE+/dBASE III Plus",
    '0x30': "Visual FoxPro",
    '0x43': "dBASE IV SQL table file without memo",
    '0x63': "dBASE IV SQL system file",
    '0x83': "FoxBASE+/dBASE IV SQL system file",
    '0x8B': "dBASE IV file with memo",
    '0xCB': "dBASE IV SQL table file with memo",
    '0xF5': "FoxPro 2.x(erlier) with memo",
    '0xFB': "FoxBASE"
}
File_info = namedtuple("File_info", ('type', 'year', 'month', 'day', 'record_count', 'header_len', 'record_len'))
FieldSpec = namedtuple('Field', ('name', 'type', 'size', 'decimal'))


def read_dbf_header(dbf_file_name):
    with open(dbf_file_name, "rb") as f:
        file_info = read_file_info(f)
        field_info = read_field_spec(f, file_info)
    return file_info, field_info


def read_file_info(f):
    file_info_data = f.read(32)
    r = list(struct.unpack("<4BLHH20x", file_info_data))
    r[0] = hex(r[0])
    file_info = File_info(*r)
    return file_info


def read_field_spec(f, file_info):
    field_info = []
    for _count in range((file_info.header_len-33-263)//32):
        field_data = f.read(32)
        name, type, size, decimal = struct.unpack('<11sc4xBB14x', field_data)
        name = ''.join([chr(c) for c in name if c > 0])
        type = chr(type[0])
        field = FieldSpec(name, type, size, decimal)
        field_info.append(field)
    return field_info


def read_records_all(f, file_info, fields_spec):
    f.seek(file_info.header_len)		                # 跳过表头区
    records_data = []			                        # 存放所有记录数据
    for _ in range(file_info.record_count):
        record_bytes = f.read(file_info.record_len)	    # 读出当前记录二进制数据
        record_value = []			                    # 存放当前的解析后记录数据
        pos = 1                                         # 第一个字节为记录删除标记
        for field_spec in fields_spec:
            field_bytes = record_bytes[pos: pos+field_spec.size]
            value = parse_field_value(field_bytes, field_spec)
            record_value.append(value)
            pos += field_spec.size
        records_data.append(record_value)
    return records_data


def parse_field_value(field_data, field_spec):
    _name = field_spec.name
    _type = field_spec.type
    _decimal = field_spec.decimal
    _size = field_spec.size

    value = field_data
    if _type in 'NFCVDL':	        # 这些类型以字符方式存储，先进行GBK解码
        value = value.replace(b'\00', b'').decode('GBK')  # 去除填充符'\00'

    # 按照具体类型进行解析（解析类型之外的数据保持原二进制格式）
    if _type == 'L':	            # 逻辑类型解析
        value = value in 'YyTt'     # False值为0x20，有些版本的True值会为Y,y,T,t
    elif _type in 'NF':	            # 数值类型解析
        if _decimal:		        # 使用Decimal可以精确表示dBase定点浮点数
            value = decimal.Decimal(value)
        else:			            # 没有小数位时使用整数类型
            value = int(value) if value.isdigit() else None
    elif _type == 'D':	            # 日期类型按照YYYYMMDD方式存储，进一步解析位datetime.date
        value = datetime.date(value[0:4], int(value[4:6]), int(value[6:8]))
    elif _type in 'BO':	            # 双精度数类型解析
        value = struct.unpack('<d', value)
    elif _type in 'I':	            # 整数类型解析
        value, = struct.unpack('<i', value)

    return value


def doctest_read_dbf_header():
    """
    >>> file_info, field_info = read_dbf_header('dbf_foxpro.dbf')
    >>> file_info
    File_info(type='0x30', year=122, month=7, day=11, record_count=3, header_len=360, record_len=6)

    >>> file_type_dict.get(file_info.type)
    'Visual FoxPro'

    >>> field_info[0]
    Field(name='a', type='I', size=4, decimal=0)

    >>> field_info[1]
    Field(name='b', type='C', size=1, decimal=0)
    """


def doctest_read_file_info():
    """
    >>> f = open("dbf_foxpro.dbf", 'rb')
    >>> file_info_data = f.read(32)

    # 读取DBF文件信息解析格式： <4BLHH20x
    # < : 小端， 4B: 4个无符号单字节整数， L: 4字节整数， H: 2字节整数， 20x: 20个字节不解析
    >>> file_type, year, month, day, record_count, header_length, record_length = \\
    ... struct.unpack('<4BLHH20x', file_info_data)
    >>> hex(file_type), year, month, day, record_count, header_length, record_length
    ('0x30', 122, 7, 11, 3, 360, 6)

    >>> field_info = []
    >>> for _count in range((header_length-33-263)//32):
    ...     field_data = f.read(32)
    ...     field = list(struct.unpack('<11sc4xBB14x', field_data))
    ...     field[0] = ''.join([chr(c) for c in field[0] if c > 0])
    ...     field_info.append(FieldSpec(*field))
    >>> for fd in field_info: print(fd)
    Field(name='a', type=b'I', size=4, decimal=0)
    Field(name='b', type=b'C', size=1, decimal=0)

    >>> f.close()
    """


def doctest_read_field_info():
    """
    >>> f = open("dbf_foxpro.dbf", 'rb')
    >>> file_info = read_file_info(f)
    >>> field_spec = read_field_spec(f, file_info)
    >>> f.close()
    >>> print(field_spec)
    [Field(name='a', type='I', size=4, decimal=0), Field(name='b', type='C', size=1, decimal=0)]
    """


def doctest_read_record():
    """
    >>> f = open("dbf_foxpro.dbf", 'rb')
    >>> file_info = read_file_info(f)
    >>> fields_spec = read_field_spec(f, file_info)
    >>> record_data = read_records_all(f, file_info, fields_spec)
    >>> f.close()
    >>> record_data
    [[0, 'x'], [1, 'y'], [2, 'z']]
    """
