# coding = utf8

import os
import filecmp
from filecmp import dircmp


def create_dir():
    if not os.path.isdir('work'):
        os.mkdir('work')
        with open("work/cmpfile1.txt", 'wt') as fp1, \
                open("work/cmpfile2.txt", 'wt') as fp2, \
                open("work/cmpfile3.txt", 'wt') as fp3:
            fp1.write("Hello-World\nHello-China")
            fp2.write("Hello World\nHello-China")
            fp3.write("Hello-World\nHello-China")
    if not os.path.isdir('work2'):
        os.mkdir('work2')
        with open("work2/cmpfile1.txt", 'wt') as fp1, \
                open("work2/cmpfile2.txt", 'wt') as fp2:
            fp1.write("Hello\nHello-China")
            fp2.write("Hello World\nHello-China")

    if not os.path.isdir('worka'):
        os.mkdir('worka')
        os.mkdir('worka/work1')
        os.mkdir('worka/work2')
        os.mkdir('worka/work3')
        with open("worka/work1/cmpfile1.txt", 'wt') as fp1, \
                open("worka/work1/cmpfile2.txt", 'wt') as fp2, \
                open("worka/work2/cmpfile1.txt", 'wt') as fp3, \
                open("worka/work3/cmpfile3.txt", 'wt') as fp4 \
                :
            fp1.write("Hello-World\nHello-China")
            fp2.write("Hello World\nHello-China")
            fp3.write("Hello-World\nHello-China")
            fp4.write("Hello-World\nHello-China")

    if not os.path.isdir('workb'):
        os.mkdir('workb')
        os.mkdir('workb/work1')
        os.mkdir('workb/work2')
        os.mkdir('workb/work3')
        os.mkdir('workb/work4')
        with open("workb/work1/cmpfile1.txt", 'wt') as fp1, \
                open("workb/work2/cmpfile1.txt", 'wt') as fp2, \
                open("workb/work2/cmpfile2.txt", 'wt') as fp3, \
                open("workb/work3/cmpfile3.txt", 'wt') as fp4:
            fp1.write("Hello-World\nHello-China")
            fp2.write("Hello-World\nHello-China")
            fp3.write("Hello World\nHello-China")
            fp4.write("Hello-World\nHello-China")


def demo_filecmp_cmpfiles():
    """
    filecmp.cmpfiles:
        compare files in dir1 and dir2 inluded in common
        return ([same files], [diff files], [error files])

    >>> create_dir()

    #shallow cmp: work-work2
    >>> print(filecmp.cmpfiles("work", "work2",
    ...                        common=["cmpfile1.txt", "cmpfile2.txt", "cmpfile3.txt"],
    ...                        shallow=True
    ...                        ))
    (['cmpfile2.txt'], ['cmpfile1.txt'], ['cmpfile3.txt'])

    # deep cmp: work-work2
    >>> print(filecmp.cmpfiles("work", "work2",
    ...                        common=["cmpfile1.txt", "cmpfile2.txt", "cmpfile3.txt"],
    ...                        shallow=False
    ...                        ))
    (['cmpfile2.txt'], ['cmpfile1.txt'], ['cmpfile3.txt'])
    """


def demo_filecmp_dircmp():
    """
    >>> create_dir()
    >>> filecmp.dircmp('work', 'work2').report()
    diff work work2
    Only in work : ['cmpfile3.txt']
    Identical files : ['cmpfile2.txt']
    Differing files : ['cmpfile1.txt']

    # diff work work2			            # 差异比较目录
    # Only in work : ['cmpfile3.txt']	    # 仅在一个目录的文件
    # Identical files : ['cmpfile2.txt']	# 相同的文件
    # Differing files : ['cmpfile1.txt']	# 不相同的文件
    """


def demo_filecmp_dircmp2():
    """
    ●─ worka [path] [files:0 dirs:3]
      └─◎─work1 [path] [files:2 dirs:0]
      │  ├─cmpfile1.txt		# 内容：Wello-World\nHello-China
      │  └─cmpfile2.txt		# 内容：Wello World\nHello-China
      └─◎─work2 [path] [files:1 dirs:0]
      │  └─cmpfile1.txt		# 内容：Wello-World\nHello-China
      └─◎─work3 [path] [files:1 dirs:0]
          └─cmpfile3.txt		# 内容：Wello-World\nHello-China
    ●─◎─workb[path] [files:0 dirs:4]
      └─◎─work1 [path] [files:1 dirs:0]
      │  └─cmpfile1.txt		# 内容：Wello-World\nHello-China
      └─◎─work2 [path] [files:2 dirs:0]
      │  ├─cmpfile1.txt		# 内容：Wello-World\nHello-China
      │  └─cmpfile2.txt		# 内容：Wello World\nHello-China
      └─◎─work3 [path] [files:1 dirs:0]
      │  └─cmpfile3.txt		# 内容：Wello-World\nHello-China
      └─◎─work4 [path] [files:0 dirs:0]

    >>> create_dir()

    dircmp report_full_closure:
    >>> filecmp.dircmp('worka', 'workb').report_full_closure()
    diff worka workb
    Only in workb : ['work4']
    Common subdirectories : ['work1', 'work2', 'work3']
    <BLANKLINE>
    diff worka\work1 workb\work1
    Only in worka\work1 : ['cmpfile2.txt']
    Identical files : ['cmpfile1.txt']
    <BLANKLINE>
    diff worka\work2 workb\work2
    Only in workb\work2 : ['cmpfile2.txt']
    Identical files : ['cmpfile1.txt']
    <BLANKLINE>
    diff worka\work3 workb\work3
    Identical files : ['cmpfile3.txt']

    # 有关比较结果的属性使用惰性计算方式，由__getattr__调用获取
    >>> cmp = filecmp.dircmp('worka', 'workb')
    >>> print(cmp.__getattr__('same_files'))		# 获取相同文件情况（使用__getattr__访问属性） +REPORT_UDIFF
    []

    >>> print(cmp.diff_files)			            # 获取不同文件情况（直接使用.方式）, 仅提供当前一层目录的比较情况
    []

    # 提供子目录比较结果
    >>> print(cmp.subdirs)			                # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    {'work1': <filecmp.dircmp object at 0x...>,
    'work2': <filecmp.dircmp object at 0x...>,
    'work3': <filecmp.dircmp object at 0x...>}

    >>> cmp.subdirs['work2'].report()    # 报告具体子目录比较结果
    diff worka\work2 workb\work2
    Only in workb\work2 : ['cmpfile2.txt']
    Identical files : ['cmpfile1.txt']

    # diff worka\work2 workb\work2
    # Only in workb\work2 : ['cmpfile2.txt']  		# 文件cmpfile2.txt仅在workb\work2中存在
    # Identical files : ['cmpfile1.txt']      		# 文件cmpfile1.txt在两个目录中存在且相同

    使用忽略ignore和隐藏hide参数设置
    >>> filecmp.dircmp('worka', 'workb', ignore=['work1'], hide=['work3']).report()
    diff worka workb
    Only in workb : ['work4']
    Common subdirectories : ['work2']
    """
