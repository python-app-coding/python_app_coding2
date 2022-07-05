# coding = utf8
"""
展示如何使用pydoc生成程序文档

>>> my_fun(1,2)
3
"""

__version__ = '1.0.0'
__author__ = 'Data APP & Service Team'
MAX_LENGTH = 1000


class MyClass:
    """
    示例类
    """

    def my_method(self):
        """
        对象方法示例
        :return: None
        """


def my_fun(a, b):
    """
    函数示例
    :param a: int
    :param b: int
    :return: int
    """
    return a + b


if __name__ == '__main__':
    my_fun(1, 2)
