# coding = utf8

import os


def test_split_path():
    """
    分割提取文件目录项：
    >>> os.path.split('E:\\work\work2\\work3/my.txt')		# 分离为路径（头部）、文件名（尾部）
    ('E:\\\\work\\\\work2\\\\work3', 'my.txt')

    >>> os.path.split('E:\\work\\work2\\work3')		# 最后一项不一定是文件
    ('E:\\\\work\\\\work2', 'work3')

    >>> os.path.splitdrive('E:\\work\\work2\\work3')		# 分离为盘符、路径文件
    ('E:', '\\\\work\\\\work2\\\\work3')

    >>> os.path.splitdrive('work\\work2\\work3')		# 不含盘符时，第1项为空串
    ('', 'work\\\\work2\\\\work3')

    >>> os.path.splitext('work\\work2\\work3.work')		# 分离出‘.’之后的扩展名部分
    ('work\\\\work2\\\\work3', '.work')

    >>> os.path.splitext('work\\work2.work\\work3')		# 只分离最后项目‘.’之后扩展部分
    ('work\\\\work2.work\\\\work3', '')
    """


def test_comm_path():
    """
    提取路径文件名公共部分：
    >>> os.path.commonpath(['E:\\work','E:\\work\\work2\\work3'])	# 提取多个路径文件名公共部分
    'E:\\\\work'

    >>> try:
    ...     os.path.commonpath(['work2','E:\\work\\work2\\work3'])	# 不能混合相对与绝对路径
    ... except ValueError as e:
    ...     print(e)
    Can't mix absolute and relative paths

    >>> try:
    ...     os.path.commonpath(['C:\\work2','E:\\work\\work2\\work3'])	# 不同驱动器下路径不能比较
    ... except ValueError as e:
    ...     print(e)
    Paths don't have the same drive

    >>> os.path.commonprefix(['/usr/lib', '/usr/local/lib'])	# 获取最长的前缀
    '/usr/l'
    """


def test_join_path():
    """
    合并路径文件名为一个有效路径文件名：
    >>> os.path.join('E:\\d1', 'd2', 'd2\\d3', 'd4')	# 合并多个路径，按照路径深度组合
    'E:\\\\d1\\\\d2\\\\d2\\\\d3\\\\d4'

    >>> os.path.join('E:\\d1', 'd2', 'C:d2\\d3', 'd4')	# 中间出现不同驱动器路径，重新开始组合
    'C:d2\\\\d3\\\\d4'

    >>> os.path.join('E:\\d1', 'd2', 'E:d2\\d3', 'd4')	# 中间出现相同驱动器相对路径，不影响组合
    'E:\\\\d1\\\\d2\\\\d2\\\\d3\\\\d4'

    >>> os.path.join('E:\\d1', 'E:\\d1\\d2', 'd3', 'd4')	# 中间出现相同驱动器相对路径，不影响组合
    'E:\\\\d1\\\\d2\\\\d3\\\\d4'
    """


def test_rel_path():
    """
    相对路径提取和计算：
    >>> os.path.relpath('E:\\d1', 'E:\\d2\\d3')		# 计算第二个路径到第一个的相对路径
    '..\\\\..\\\\d1'

    >>> os.path.relpath('E:\\d1', 'E:\\d2\\d3')		# 最好不使用相对路径，会产生难以解释结果
    '..\\\\..\\\\d1'

    >>> try:
    ...     os.path.relpath('d:\\d1', 'E:d2\\d3')	# 使用不同盘符，无法进行计算
    ... except ValueError as e:
    ...     print(e)
    path is on mount 'd:', start on mount 'E:'
    """

