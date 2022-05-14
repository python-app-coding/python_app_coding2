# coding: utf8

"""
展示随机读写文本行模块linecache的使用
"""

import linecache as lc


def create_text_file(file_name="temp_text.txt", line_num=10, fixed_length=True):
    with open(file_name, "w", encoding="utf8") as fp:
        if fixed_length:
            fp.writelines([f"Line-{j+1}\n" for j in range(line_num)])
        else:
            fp.writelines([f"Line-{j+1}:"+f"{j+1}"*(j+1)+"\n" for j in range(line_num)])


def read_fixedlen_line_by_open(file_name, line_no: int = 1):
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


if __name__ == "__main__":
    temp_file = "temp_fixedlen.txt"
    create_text_file(file_name=temp_file)
    line = read_fixedlen_line_by_open(file_name=temp_file, line_no=9)
    print(line)
    temp_file = "temp_varlen.txt"
    create_text_file(file_name=temp_file, fixed_length=False)
    line = read_varlen_line_by_open(file_name=temp_file, line_no=5)
    print(line)
    line = read_line_by_linecache(file_name=temp_file, line_no=5)
    print(line)

