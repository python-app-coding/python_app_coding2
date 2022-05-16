# coding: utf8
"""
演示在open函数中设置newline的各种效果和影响
demo the usage of parameter newline in open function
"""
import os

demo_text = "Line1\nLine2\rLine3\r\n"
demo_file = "temp_newline.txt"


def demo_open_write_with_newline(filename=demo_file, newline=None):
    """
    展示使用open函数写文本文件时newline的作用
    将newline分别设置为None, "\n", "", "\r"时，文本写入文件的情况
    demo what happens when writing text by open to file if newline is set to None, "\n", "", "\r", "\r\n"

    newline在写文本文件时的作用 newline behaviors in writing text file:
    newline=None，使用universal Newline模式（PEP278），文本中的“\n”被视为换行符，写入时将其转换为os.linesep；
    newline="\n", 写入时对文本内容不做任何替换；
    newline="", 写入时对文本内容不做任何替换；
    newline="\r", 写入时将"\n"转换为“\r”；
    newline="\r\n", 写入时将"\n"转换为“\r\n”；

    总结 Summary:
    在将文本写入文件时，希望将'\n'转换为操作系统规定的换行符，可使用newline=None;
    在将文本写入文件时，希望将'\n'转换为'\r'，可使用newline='\r'；
    在将文本写入文件时，希望将'\n'转换为'\r\n'，可使用newline='\r\n'；
    在将文本写入文件时，希望保持原文本不变，可使用newline='\n'或‘’。
    """

    print("\n\nwrite text to file\n"+'-'*100)

    # display newline char and raw text string
    newline_str = str(newline.encode('utf8')) if isinstance(newline, str) else "None"
    print(f"newline={newline_str}")
    print("raw text:", demo_text.encode('utf8'))

    # write demo_text to file with newline
    with open(filename, "w+", newline=newline, encoding="utf8") as fp:
        fp.write(demo_text)

    # read from text file in binary mode to compare with raw_text
    with open(filename, "rb") as fp:
        readbytes = fp.read()
        if newline is None:
            print("write to:", readbytes, "\t# " +
                  r"\n ==> os.linesep (os.linesep is '\r\n' in Windows, '\n' in Linux, '\r' in Mac)")
        elif newline in ("", "\n"):
            print("write to:", readbytes, "\t# "+r" no conversion")
        elif newline == "\r":
            print("write to:", readbytes, "\t# " + r" \n ==> \r")
        elif newline == "\r\n":
            print("write to:", readbytes, "\t# " + r" \n ==> \r\n")
        else:
            # so far, the legal_newline_char can be None, '', '\n', '\r', and '\r\n'
            print("write to:", readbytes, "\t# "+r" \n ==> "+str(newline.encode('utf8')))


def demo_open_read_with_newline(filename=demo_file, newline=None):
    """
    展示读文本文件时，设置newline的效果
    分别设置为None, “”， "\n", "\r"时，文本文件读出数据的情况
    demo what happens when reading text from text file if newline is set to None, "\n", "", "\r", "\r\n"

    设置newline对open.read和readline(s)的影响 newline behaviors in reading text file by open.read or readline:
    newline=None，将文本中的'\r', '\n' '\r\n'都视为行结束符，读出后都转换为'\n';
    newline='', 将文本中的'\r', '\n' '\r\n'都视为行结束符，读出内容不做转换;
    newline='\r', 将文本中的'\r'视为行结束符，读出内容不做转换;
    newline='\n', 将文本中的'\n'视为行结束符，读出内容不做转换;
    newline='\r\n', 将文本中的'\r\n'视为行结束符，读出内容不做转换;

    总结 Summary:
    如果将文件中的'\r', '\n' '\r\n'都视为行结束符，读出后进仅使用'\n'做行结束符，使用newline=None读出最合适;
    如果将文件中的'\r', '\n' '\r\n'都视为行结束符，对文件的内容不做改变，使用newline=''最合适；
    如果针对文件的'\r', '\n' '\r\n'分别处理行结束符，需要按照配置使用newline。
    """

    with open(filename, "w+", newline="", encoding="utf8") as fp:
        fp.write(demo_text)
    with open(filename, "rb") as fp:
        demo_text_in_file = fp.read()

    print("\n\nread text from file\n"+'-'*80)
    newline_str = str(newline.encode('utf8')) if isinstance(newline, str) else "None"
    print(f"newline={newline_str}")
    print("raw text:", demo_text_in_file)
    with open(filename, mode="r", newline=newline) as fp:
        # read by read
        readbytes = fp.read().encode('utf8')
        if newline is None:
            print("read  to:", readbytes, "\t# no replace")
        elif newline == "":
            print("read  to:", readbytes, "\t# no replace")
        elif newline == "\r":
            print("read  to:", readbytes, "\t# no replace")
        elif newline == "\n":
            print("read  to:", readbytes, "\t# no replace")
        else:
            print("read  to:", readbytes, "\t# no replace")
        print("-."*40)
        # read by readlines
        print(f"# use {newline_str} as line-end-char to get each line")
        print("--- readlines ---")
        fp.seek(0)
        for lno, line in enumerate(fp.readlines()):
            print(f"(line-{lno+1}):{line.encode('utf8')}")
        print("--- readline ---")
        fp.seek(0)
        line_no = 1
        while True:
            line = fp.readline()
            if line == "":
                break
            print(f"(line-{line_no}):{line.encode()}")
            line_no += 1


if __name__ == "__main__":
    print(f"os.linesep={os.linesep.encode()}")

    # demo write
    demo_open_write_with_newline(newline=None)
    demo_open_write_with_newline(newline='')
    demo_open_write_with_newline(newline='\n')
    demo_open_write_with_newline(newline='\r')
    demo_open_write_with_newline(newline='\r\n')
    # demo_open_write_with_newline(newline='\n\r')  # invalid newline char

    # demo read
    # demo_open_read_with_newline(newline=None)
    # demo_open_read_with_newline(newline="")
    # demo_open_read_with_newline(newline="\r")
    # demo_open_read_with_newline(newline="\n")
    # demo_open_read_with_newline(newline="\r\n")
