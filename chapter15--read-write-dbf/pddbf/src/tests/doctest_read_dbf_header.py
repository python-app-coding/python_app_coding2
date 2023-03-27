# coding: utf8

# import os
import struct
from collections import namedtuple


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
    field_info = []
    with open(dbf_file_name, "rb") as f:
        # get file info
        file_info_data = f.read(32)
        r = list(struct.unpack("<4BLHH20x", file_info_data))
        r[0] = hex(r[0])
        file_info = File_info(*r)

        # get field info
        for _count in range((file_info.header_len-33-263)//32):
            # byte1 = f.read(1)
            # if byte1 == b'r':
            #     break
            # field_data = byte1 + f.read(31)
            field_data = f.read(32)
            name, type, size, decimal = struct.unpack('<11sc4xBB14x', field_data)
            name = ''.join([chr(c) for c in name if c > 0])
            type = chr(type[0])
            field = FieldSpec(name, type, size, decimal)
            # field = FieldSpec(*struct.unpack('<11sc4xBB14x', field_data))
            field_info.append(field)
    return file_info, field_info


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
    >>> file_info_data = f.read(32)
    """



if __name__ == '__main__':
    print(read_dbf_header('dbf_foxpro.dbf'))
    print(read_dbf_header('dbf_with_cn.dbf'))
    print(read_dbf_header('dbf_with_null.dbf'))
