# coding: utf8

import os
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


def test_header():
    """
    >>> with open("temp.dbf", "rb") as fp:
    ...    data_info = fp.read(32)
    ...    r = list(struct.unpack("<B3BLHH20x", data_info))
    ...    r[0] = hex(r[0])
    ...    print("{}, {}, {}, {}, {}, {}, {}".format(*r))
    0x30, 122, 7, 11, 3, 360, 6

    >>> file_type = r[0]
    >>> file_type_dict.get(r[0])
    'Visual FoxPro'

    >>> file_info = File_info(*r)
    >>> file_info
    File_info(type='0x30', year=122, month=7, day=11, record_count=3, header_len=360, record_len=6)
    """




if __name__ == '__main__':
    test_header()

