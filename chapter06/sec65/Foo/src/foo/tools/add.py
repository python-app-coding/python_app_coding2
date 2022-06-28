# coding = utf8
"""
main是foo的模块，作为main的入口模块
"""


def add(*args):
    """
    函数，位于foo包的__main__文件内
    function in foo.__main__

    Args:
        args：sequence

    Return:
        digital(int, float)


    >>> add(10, 20)
    30
    """
    return sum(args)


def add2(a, b):
    """
    function in main
    add addends, return sum

    Args:
        a(float/int): addend 加数
        b(float/int): addend 加数

    Return:
        sum(float/int) 和

    >>> add2(10, 20)
    200
    """
    return a + b
