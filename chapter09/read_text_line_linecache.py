# coding: utf8

"""
展示随机读写文本行模块linecache的使用
"""

import linecache as lc
import os


def create_text_file(file_name="temp_text.txt", line_num=10, fixed_length=True):
    with open(file_name, "w", encoding="utf8") as fp:
        if fixed_length:
            fp.writelines([f"Line-{j+1}\n" for j in range(line_num)])
        else:
            fp.writelines([f"Line-{j+1}:"+f"{j+1}"*(j+1)+"\n" for j in range(line_num)])


def read_fixedlen_line_by_open(file_name, line_no: int = 1):
    """
    使用open(newline="")，对读出内容不做转换，可以准确确定行字符数
    """
    with open(file_name, "r", encoding="utf8", newline="") as fp:
        if line_no <= 0:
            raise ValueError
        line_length = len(fp.readline())
        fp.seek(line_length*(line_no-1), 0)
        # rs = fp.readline()
        # rs = fp.readline()
        # print(line_length, line_length*(line_no-1), rs)
        return fp.readline()


def read_varlen_line_by_open(file_name, line_no=1):
    with open(file_name, "r", encoding="utf8") as fp:
        for j in range(line_no-1):
            fp.readline()
        return fp.readline()


def read_line_by_linecache(file_name, line_no=1):
    return lc.getline(filename=file_name, lineno=line_no)


def read_text_file(fname):
    with open(fname, mode="r", encoding='utf8', newline='\r\n') as fp:
        print(f"text in file: {fname}\n"+"-"*30)
        for line in fp.readlines():
            print(line, end="")
        print("\n")


if __name__ == "__main__":
    temp_file_fixedlen = "temp_fixedlen.txt"
    temp_file_varlen = "temp_varlen.txt"
    line_no = 6

    if not os.path.isfile(temp_file_fixedlen):
        create_text_file(file_name=temp_file_fixedlen)
    if not os.path.isfile(temp_file_varlen):
        create_text_file(file_name=temp_file_varlen, fixed_length=False)

    # display file content
    read_text_file(temp_file_fixedlen)
    read_text_file(temp_file_varlen)

    print("read fixed-line-length text file by open")
    line = read_fixedlen_line_by_open(file_name=temp_file_fixedlen, line_no=line_no)
    print(f"file: {temp_file_fixedlen} \nline-{line_no}: {line}")

    print("read var-line-length text file by open")
    line = read_varlen_line_by_open(file_name=temp_file_varlen, line_no=line_no)
    print(f"file: {temp_file_varlen} \nline-{line_no}: {line}")

    print("read var-line-length text file by linecache")
    line = read_line_by_linecache(file_name=temp_file_varlen, line_no=line_no)
    print(f"file: {temp_file_varlen} \nline-{line_no}: {line}")

