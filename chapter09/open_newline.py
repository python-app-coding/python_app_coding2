# coding: utf8
"""
演示在open函数中设置newline的各种效果和影响
demo the usage of parameter newline in open function
"""


demo_text = "Line1\nLine2\rLine3\r\n"


def demo_open_write_with_newline(filename="demo_newline.txt", newline=None):
    """
    展示写文本文件时newline的作用
    将newline分别设置为None, "\n", "", "\r"时，文本写入文件的情况
    demo what happens when writing text to file
    if newline is set to None, "\n", "", "\r", etc

    test result:
    newline=None，将文本中的“\r”转换为os.linesep，
    newline="\n" or "", 不做任何替换
    newline=any_legal_char, 定义：将\n替换为any_legal_char，
        测试：对合法字符的定义不明确，各种其它字符对写数据没有进行替换
    """

    if newline is None:
        # newline=None
        # 写入文件时，以\n为行结束符，转换为os.linesep()
        print("newline=None")
        with open(filename, "w+", newline=None, encoding="utf8") as fp:
            fp.write(demo_text)
        with open(filename, "rb") as fp:
            readbytes = fp.read()
            print("raw text:", demo_text.encode('utf8'))
            print("write to:", readbytes, "\t# "+r"\n ==> os.linesep (os.linesep is '\r\n' in Windows)")

    if newline in ["\n", ""]:
        # newline="\n"
        # 写入文件时,对原文本不做转换
        print(r"newline='\n'")
        with open(filename, "w+", newline="\n", encoding="utf8") as fp:
            fp.write(demo_text)
        with open(filename, "rb") as fp:
            readbytes = fp.read()
            print("raw text:", demo_text.encode('utf8'))
            print("write to:", readbytes, "\t# "+r" no replacement")
        # newline=""
        # 写入文件时,对原文本不做转换
        print("newline=''")
        with open(filename, "w+", newline="", encoding="utf8") as fp:
            fp.write(demo_text)
        with open(filename, "rb") as fp:
            readbytes = fp.read()
            print("raw text:", demo_text.encode('utf8'))
            print("write to:", readbytes, "\t# "+r" no replacement")

    if newline == "\r":
        # newline="\n"
        # 写入文件时,对原文本不做转换
        print(r"newline='\r'")
        with open(filename, "w+", newline="\r", encoding="utf8") as fp:
            fp.write(demo_text)
        with open(filename, "rb") as fp:
            readbytes = fp.read()
            print("raw text:", demo_text.encode('utf8'))
            print("write to:", readbytes, "\t# " + r" \n ==> \r")

    if newline not in ["\n", "", "\r", None]:
        # newline="\n"
        # 写入文件时,对原文本不做转换
        print(("newline="+newline).encode('utf8'))
        with open(filename, "w+", newline="\n", encoding="utf8") as fp:
            fp.write(demo_text)
        with open(filename, "rb") as fp:
            readbytes = fp.read()
            print("raw text:", demo_text.encode('utf8'))
            print("write to:", readbytes, "\t# "+r" \n ==> "+str(newline.encode('utf8'))+"?")


def demo_open_read_with_newline(filename="demo_newline.txt", newline=None):
    """
    展示读文本文件时，设置newline的效果
    分别设置为None, “”， "\n", "\r"时，文本文件读出数据的情况
    demo what happens when reading text from text file
    if newline is set to None, "\n", "", "\r", etc

    test result:
    newline=None，将文本中的'\r', '\n' '\r\n'都视为行结束符，都转换为'\n'
    newline='',
    newline='\r',
    newline='\n',
    newline=any_legal_char,
    """
    
    with open(filename, "w+", newline=None, encoding="utf8") as fp:
        fp.write(demo_text)

    print("read from demo file")
    if newline is None:
        # newline=None
        # 写入文件时，以\n为行结束符，转换为os.linesep()
        print("newline=None")
        with open(filename, mode="r", newline=None) as fp:
            readbytes = fp.read().encode('utf8')
            print("raw text:", demo_text.encode('utf8'))
            print("read  to:", readbytes, "\t# "+r"'\r', '\n' '\r\n' ==> '\n'")


if __name__ == "__main__":
    demo_open_write_with_newline(newline=None)
    demo_open_write_with_newline(newline='\n')
    demo_open_write_with_newline(newline='\r')
    demo_open_write_with_newline(newline='\r\n')
    demo_open_write_with_newline(newline='\b')

    demo_open_read_with_newline(newline=None)
