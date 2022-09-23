# coding: utf8
"""
演示在open函数中设置newline的各种效果和影响
demo the usage of parameter newline in open function
"""
import os

demo_text = "Line1\nLine2\rLine3\r\n"
demo_lines = ["Line1\n", "Line2\r", "Line3\r\n"]
demo_file = "temp_newline.txt"
demo_file2 = "temp_newline2.txt"


def demo_open_read_with_newline(newline=None):
    """
    展示读文本文件时，设置newline的效果
    分别设置为None, “”， "\n", "\r"时，文本文件读出数据的情况
    demo what happens when reading text from text file if newline is set to None, "\n", "", "\r", "\r\n"

    【设置newline】
    设置newline对open.read和readline(s)的影响 newline behaviors in reading text file by open.read or readline:
    newline=None，将文本中的'\r', '\n' '\r\n'都视为行结束符，读出后都转换为'\n';
    newline='', 将文本中的'\r', '\n' '\r\n'都视为行结束符，读出内容不做转换;
    newline='\r', 将文本中的'\r'视为行结束符，读出内容不做转换;
    newline='\n', 将文本中的'\n'视为行结束符，读出内容不做转换;
    newline='\r\n', 将文本中的'\r\n'视为行结束符，读出内容不做转换;

    【总结 Summary】
    读出数据时，只有newline=None会进行换行符转换，
    其余设置用于识别换行符，对分行读出内容产生作用。
    如果将文件中的'\r', '\n' '\r\n'都视为行结束符，读出后都转为'\n'，使用newline=None;
    如果将文件中的'\r', '\n' '\r\n'都视为行结束符，读出后不做改变，使用newline=''；
    如果将文件种的'\r'视为行结束符，使用newline='\r';
    如果将文件种的'\n'视为行结束符，使用newline='\n';
    如果将文件种的'\r\n'视为行结束符，使用newline='\r\n'.
    """

    with open(demo_file, "w+", newline="", encoding="utf8") as fp:
        fp.write(demo_text)
    with open(demo_file, "rb") as fp:
        demo_text_in_file = fp.read()

    print("\n\nread text from file\n"+'-'*80)
    newline_str = str(newline.encode('utf8')).replace('b', '') if isinstance(newline, str) else "None"
    print(f"newline={newline_str}")
    print("raw text:", str(demo_text_in_file)[1:])
    with open(demo_file, mode="r", newline=newline) as fp:
        # encode read text to bytestring for display
        readbytes = fp.read().encode('utf8')
        readbytes = str(readbytes)[1:]      # remove b at first pos
        if newline is None:
            print("read  to:", readbytes, "\t# replace: \\n, \\r, \\r\\n --> \\n")
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
            linestr = str(line.encode('utf8'))[1:]
            print(f"(line-{lno+1}):{linestr}")

        print("--- readline ---")
        fp.seek(0)
        line_no = 1
        while True:
            line = fp.readline()
            if line == "":
                break
            line = str(line.encode())[1:]
            print(f"(line-{line_no}):{line}")
            line_no += 1


def demo_open_write_with_newline(newline=None):
    """
    展示使用open函数写文本文件时newline的作用
    将newline有5种设置， 分别为{None "\n", "", "\r", "\r\n"}，对文本写入文件具有不同影响。
    demo what happens when writing text file with open
    if newline is set to 5 modes: None, "\n", "", "\r", "\r\n".

    【设置newline对写文本文件的作用】
    newline effect on writing text file
    1) newline=None，使用universal Newline模式（PEP278），文本中的“\n”被视为换行符，写入时将其转换为os.linesep；
    2) newline="\n", 写入时对文本内容不做任何替换；
    3) newline="", 写入时对文本内容不做任何替换；
    4) newline="\r", 写入时将"\n"转换为“\r”；
    5) newline="\r\n", 写入时将"\n"转换为“\r\n”；

    【总结 Summary】
    Python文本以'\n'为行分隔符，将文本写入文本文件时， 应考虑newline设置的影响。
    1） 将文本写入文件时，希望将'\n'转换为操作系统规定的换行符，可使用newline=None;
    2） 将文本写入文件时，希望将'\n'转换为'\r'，可使用newline='\r'；
    3） 将文本写入文件时，希望将'\n'转换为'\r\n'，可使用newline='\r\n'；
    4） 将文本写入文件时，希望保持原文本不变，可使用newline='\n'或''。
    """

    print("\n\nwrite text to file\n"+'-'*100)

    # display newline char and raw text string
    newline_str = str(newline.encode('utf8')).replace('b', '') if isinstance(newline, str) else "None"
    print(f"newline={newline_str}", end='')
    if newline is None:
        print("\treplace: "+r"\n ==> os.linesep ('\r\n' in Windows, '\n' in Linux, '\r' in Mac)")
    elif newline in ("", "\n"):
        print("\treplace: "+" no replace")
    elif  newline == "\r":
        print("\treplace: " + r" \n ==> \r")
    elif newline == "\r\n":
        print("\treplace: "+r" \n ==> \r\n")
    else:
        # so far, the legal_newline_char can be None, '', '\n', '\r', and '\r\n'
        print("\t# "+r" \n ==> "+str(newline.encode('utf8')))

    print("raw text:", str(demo_text.encode('utf8'))[1:])

    # write demo_text to file with newline=None
    with open(demo_file, "w+", newline=newline, encoding="utf8") as fp:
        fp.write(demo_text)

    # read from text file in binary mode to compare with raw_text
    with open(demo_file, "rb") as fp:
        readbytes = fp.read()
        readbytes = str(readbytes)[1:]  # remove b at first pos
        if newline is None:
            print("write to:", readbytes)
        elif newline in ("", "\n"):
            print("write to:", readbytes)
        elif newline == "\r":
            print("write to:", readbytes)
        elif newline == "\r\n":
            print("write to:", readbytes)
        else:
            print("write to:", readbytes)

    # write demo_text to file2 with writelines
    print("raw lines: ", demo_lines)
    with open(demo_file2, "w+", newline=newline, encoding="utf8") as fp:
        fp.writelines(demo_lines)
    with open(demo_file2, "rb") as fp:
        readbytes = fp.read()
        readbytes = str(readbytes)[1:]  # remove b at first pos
        print("writelines to:", readbytes)


def demo_open_u_mode():
    print('raw text:')
    print(r'Hello World\r\nHello China\nHello Shandong')

    with open('temp_open_u_mode.txt', mode='w') as fp:
        fp.write('Hello World\r\nHello China\nHello Shandong')

    print('\nwritten text:')
    with open('temp_open_u_mode.txt', 'rb') as fp:
        print(str(fp.read())[1:])

    print('\nread text mode=rU:')
    # 'U' mode is deprecated
    with open('temp_open_u_mode.txt', 'rU') as fp:
        rtext = fp.read()
        print(rtext.encode()[1:])


if __name__ == "__main__":
    print(f"os.linesep={os.linesep.encode()}")

    demo1 = True
    if demo1:
        # demo write
        demo_open_write_with_newline(newline=None)
        demo_open_write_with_newline(newline='')
        demo_open_write_with_newline(newline='\n')
        demo_open_write_with_newline(newline='\r')
        demo_open_write_with_newline(newline='\r\n')

    demo2 = True
    if demo2:
        # demo read
        demo_open_read_with_newline(newline=None)
        demo_open_read_with_newline(newline="")
        demo_open_read_with_newline(newline="\r")
        demo_open_read_with_newline(newline="\n")
        demo_open_read_with_newline(newline="\r\n")

    demo3 = False
    # mode u is deprecated now!
    if demo3:
        demo_open_u_mode()
