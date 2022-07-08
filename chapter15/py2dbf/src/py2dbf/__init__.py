# coding = utf8
"""
py2dbf提供的基本调用接口和类
read_dbf： 读取dbf文件的函数接口，传递一个文件名参数，返回DataFrame数据集
write_dbf: 将DataFrame写为dbf文件，传递一个文件名参数，完成写dbf文件操作。无返回值。
Dbf： 读写dbf文件的类。调用DbfReader和DbfWriter。
    类属性：
    encoding：str。读写dbf文件使用的编码。dbf文件需要使用GBK编码存储汉字，如果dbf中包含汉字，应设置为'GBK'
    对象属性：
    data：DataFrame数据。读取dbf文件的数据后存到data，写dbf文件时，将data写到dbf
    reader：DbfReader对象，用于读取dbf文件。
    delflag：保存原dbf文件中的删除标记。不用于写dbf文件。
    方法：
    open: 打开dbf文件。
    fetch：获取dbf文件记录数据。
    close：关闭dbf文件。
DbfReader：读取dbf文件底层类。
DbfWriter：写DataFrame到dbf文件的底层类。
"""
__version__ = '1.0.1'
__author__ = 'Wang Xichang'

from .pydbf import Dbf, read_dbf, write_dbf, DbfReader, DbfWriter

__all__ = ['Dbf', read_dbf, write_dbf, 'DbfReader', 'DbfWriter']
