# coding = utf8

import filecmp
import difflib
import shutil
import os

def create_files():
    """
    create same or similar content text files:
    cmpfile1 ~= cmpfile2
    cmpfile1 == cmpfile3
    """
    if not os.path.isdir('work'):
        os.mkdir('work')
        with open("work/cmpfile1.txt", 'wt') as fp1, \
                open("work/cmpfile2.txt", 'wt') as fp2, \
                open("work/cmpfile3.txt", 'wt') as fp3:
            fp1.write("Hello-World\nHello-China")
            fp2.write("Hello+World\nHello-China")
            fp3.write("Hello-World\nHello-China")


def demo_filecmp():
    """
    >>> create_files()

    # >>> os.stat("work/cmpfile1.txt")
    # >>> os.stat("work/cmpfile2.txt")
    # >>> os.stat("work/cmpfile3.txt")

    >>> filecmp.cmp("work/cmpfile1.txt", "work/cmpfile2.txt")
    True
    >>> filecmp.cmp("work/cmpfile1.txt", "work/cmpfile2.txt", shallow=False)
    False
    >>> filecmp.cmp("work/cmpfile1.txt", "work/cmpfile3.txt", shallow=False)
    True
    """


def demo_difflib():
    """
    >>> with open("cmpfile01.txt", 'wt') as fp01, \\
    ...         open("cmpfile02.txt", 'wt') as fp02:
    ...      fp01.writelines(
    ...          "this is line01\\n"
    ...          "this is line02\\n"
    ...          "this is line03\\n")
    ...      fp02.writelines(
    ...          "this is line0102\\n"
    ...          "this is line02\\n"
    ...          "this is line0203\\n"
    ...          "this is line0204\\n")

    # 使用Differ对象的compare方法比较两个字符串文本
    >>> with open('cmpfile01.txt') as fp1, open('cmpfile02.txt') as fp2:
    ...     lines1 = fp1.readlines()
    ...     lines2 = fp2.readlines()
    ...     for line in difflib.Differ().compare(lines1, lines2):
    ...         print(line, end='')
    - this is line01
    + this is line0102
    ?               ++
      this is line02
    - this is line03
    + this is line0203
    ?              ++
    + this is line0204

    # 比较结果(-: 第一文件的文本， +: 第二文件的文本， ？: 标识差异位置， ' ':两个文本行相同的内容)
    # - this is line01
    # + this is line0102
    # ?               ++	# 在该位置出现不同
    #   this is line02	# 该行都相同
    # - this is line03
    # + this is line0203
    # ?              ++	# 在该位置出现不同
    # + this is line0204	# 该行只在第二个文件存在

    # 使用SequenceMatcher对象的get_matching_blocks方法进行比较
    >>> s = difflib.SequenceMatcher(a="abxcd", b="abcd")	# 比较两个文本序列
    >>> cr = s.get_matching_blocks()	                    # 比较结果是元素为命名元组的列表
    >>> for m in cr:
    ...     print(m)
    Match(a=0, b=0, size=2)
    Match(a=3, b=2, size=2)
    Match(a=5, b=4, size=0)

    # Match(a=0, b=0, size=2),			# 0位置开始2个字符相同,即a[0:2] == b[0:2]
    # Match(a=3, b=2, size=2), 			# a=3,b=2位置，2个字符相同,a[3:5] == b[2:4]
    # Match(a=5, b=4, size=0)			# 最后一个是无效结果（dummy）
    """
