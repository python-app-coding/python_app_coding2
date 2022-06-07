# coding = utf8

import pathlib
import os


def test_pathlib_path_touch(filename):
    """
    测试使用pathlib.Path.touch创建空文件
    :param filename:
    :return:
    >>> pobj = pathlib.Path('temp_file.txt')	            		    # 创建Path对象
    >>> pobj.touch()				# 创建空文件
    >>> os.path.isfile('temp_file.txt')		                            # 检查是否创建成功
    True
    >>> try:
    ...     pathlib.Path('temp_file.txt').touch(exist_ok=False)       	# 文件存在时，设置exist_ok触发异常
    ... except FileExistsError as e:
    ...     print(e)
    [Errno 17] File exists: 'temp_file.txt'

    Traceback (most recent call last):
     ......
    FileExistsError: [Errno 17] File exists: 'temp_file.txt'
    """
