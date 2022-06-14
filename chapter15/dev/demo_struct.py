# coding = utf8

import struct


def demo_struct():
    """
    demo how to use struct to pack objects to data , and unpack data to objects

    >>> struct.pack('hhl', 1, 2, 3)	# 按照格式分别将三个变量编码为：短整数h、短整数h、整数l
    b'\x00\x01\x00\x02\x00\x00\x00\x03'	# 分别占用字节数：2，2，4，注意：都使用了缺省字节顺序

    # 这是使用缺省字节顺序的结果，说明本机器使用'大端'方式
    # 解码结果为各变量的元组
    >>> struct.unpack('hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03')	# 使用同样方式unpack
    (1, 2, 3)

    # 可以计算格式码的总字节数
    >>> struct.calcsize('hhl')
    8

    >>> struct.pack('<hhl', 1, 2, 3)			# 按照设定的小端格式
    b'\x01\x00\x02\x00\x03\x00\x00\x00'			# 低位的字节在最前面

    # unpack出的数值不对！
    >>> struct.unpack('>hhl', b'\x01\x00\x02\x00\x03\x00\x00\x00')	# 使用不同的字节顺序unpack会出错
    (256, 512, 50331648)
    """
