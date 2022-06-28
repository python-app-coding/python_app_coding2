# coding = utf8
"""
属于子包subfoo的模块
使用模块方式运行时显示文件所在的绝对路径

> py -m path

.../path.py
"""

import os
import sys


def abspath(path='c:/'):
    """函数功能
       输出一个路径的绝对路径

       Args:
           path(str): 输入路径

       Returns:
           None

       Output:
           abs path = <abspath(path)>

    >>> abspath('c:/')
    'c:\\\\'
    """
    return os.path.abspath(path)
