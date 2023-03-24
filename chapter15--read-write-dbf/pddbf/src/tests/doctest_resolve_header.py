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


def read_field_spec(f, header_len):
    field_info = []
    for _count in range((header_len-33-263)//32):
        byte1 = f.read(1)
        if byte1 == b'r':
            break
        field_data = byte1 + f.read(31)
        field = FieldSpec(*struct.unpack('<11sc4xBB14x', field_data))
        field_info.append(field)
    return field_info


def read_dbf_header():
    """
    >>> with open("demo_foxpro.dbf", "rb") as f:
    ...    data_info = f.read(32)
    ...    r = list(struct.unpack("<4BLHH20x", data_info))
    ...    r[0] = hex(r[0])
    ...    print("{}, {}, {}, {}, {}, {}, {}".format(*r))
    0x30, 122, 7, 11, 3, 360, 6

    >>> file_type = r[0]
    >>> file_type_dict.get(r[0])
    'Visual FoxPro'

    >>> file_info = File_info(*r)
    >>> file_info
    File_info(type='0x30', year=122, month=7, day=11, record_count=3, header_len=360, record_len=6)

    >>> field_info = []
    >>> with open("demo_foxpro.dbf", "rb") as f:
    ...    f.read(32)
    ...    for _count in range((file_info.header_len-33-263)//32):
    ...        field_data = f.read(32)
    ...        name, type, size, decimal = struct.unpack('<11sc4xBB14x', field_data)
    ...        name = ''.join([chr(c) for c in name if c > 0])
    ...        type = chr(type[0])
    ...        field = FieldSpec(name, type, size, decimal)
    ...        field_info.append(field)
    >>> field_info
    Field(name='a', type='I', size=4, decimal=0), Field(name='b', type='C', size=1, decimal=0)
    """


if __name__ == '__main__':
    read_dbf_header()

