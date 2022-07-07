# coding: utf8

"""
展示随机读写文本行模块linecache的使用
"""

import linecache as lc
import os

temp_file_fixedlen = "temp_fixedlen.txt"
temp_file_varlen = "temp_varlen.txt"
line_no = 6


def create_text_file(file_name="temp_text.txt", line_num=10, fixed_length=True):
    with open(file_name, "w", encoding="utf8") as fp:
        if fixed_length:
            fp.writelines([f"Line-{j+1}\n" for j in range(line_num)])
        else:
            fp.writelines([f"Line-{j+1}:"+f"{j+1}"*(j+1)+"\n" for j in range(line_num)])


def read_text_file(fname):
    with open(fname, mode="r", encoding='utf8', newline='\r\n') as fp:
        print(f"text in file: {fname}\n"+"-"*30)
        for line in fp.readlines():
            print(line, end="")
        print("\n")


def make_files():
    if not os.path.isfile(temp_file_fixedlen):
        create_text_file(file_name=temp_file_fixedlen)
    if not os.path.isfile(temp_file_varlen):
        create_text_file(file_name=temp_file_varlen, fixed_length=False)

    # display file content
    read_text_file(temp_file_fixedlen)
    read_text_file(temp_file_varlen)



def read_fixedlen_line_by_open(file_name, line_no: int = 1):
    """
    按指定行号读出固定行长度文本文件中的行
    使用open(newline="")，对读出内容不做转换，可以准确确定行字符数

    >>> make_files()    # doctest: +NORMALIZE_WHITESPACE
    text in file: temp_fixedlen.txt
    ------------------------------
    Line-1
    Line-2
    Line-3
    Line-4
    Line-5
    Line-6
    Line-7
    Line-8
    Line-9
    Line-10
    <BLANKLINE>
    <BLANKLINE>
    text in file: temp_varlen.txt
    ------------------------------
    Line-1:1
    Line-2:22
    Line-3:333
    Line-4:4444
    Line-5:55555
    Line-6:666666
    Line-7:7777777
    Line-8:88888888
    Line-9:999999999
    Line-10:10101010101010101010
    <BLANKLINE>
    <BLANKLINE>

    read fixed-line-length text file by open
    >>> line = read_fixedlen_line_by_open(file_name=temp_file_fixedlen, line_no=line_no)
    >>> print(f"file: {temp_file_fixedlen} \\nline-{line_no}: {line}")      # doctest: +NORMALIZE_WHITESPACE
    file: temp_fixedlen.txt
    line-6: Line-6
    <BLANKLINE>
    """
    with open(file_name, "r", encoding="utf8", newline="") as fp:
        if line_no <= 0:
            raise ValueError
        line_length = len(fp.readline())
        fp.seek(line_length*(line_no-1), 0)
        return fp.readline()


def read_varlen_line_by_open(file_name, line_no=1):
    """
    使用open函数，根据指定行号读出变长行的文本行
    read var-line-length text file by open

    >>> line = read_varlen_line_by_open(file_name=temp_file_varlen, line_no=line_no)
    >>> print(f"file: {temp_file_varlen} \\nline-{line_no}: {line}")     # doctest: +NORMALIZE_WHITESPACE
    file: temp_varlen.txt
    line-6: Line-6:666666
    <BLANKLINE>
    """
    with open(file_name, "r", encoding="utf8") as fp:
        for j in range(line_no-1):
            fp.readline()
        return fp.readline()


def read_line_by_linecache(file_name, line_no=1):
    """
    使用linecache.getline方法，根据指定行号读出变长行的文本行
    read var-line-length text file by linecache.getline

    >>> line = read_line_by_linecache(file_name=temp_file_varlen, line_no=line_no)
    >>> print(f"file: {temp_file_varlen} \\nline-{line_no}: {line}")     # doctest: +NORMALIZE_WHITESPACE
    file: temp_varlen.txt
    line-6: Line-6:666666
    <BLANKLINE>
    """
    return lc.getline(filename=file_name, lineno=line_no)



