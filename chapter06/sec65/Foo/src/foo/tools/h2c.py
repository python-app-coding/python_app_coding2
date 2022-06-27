# coding = utf8

"""
华氏温度与摄氏温度值转换
"""


def f_c(f):
    """
    华氏温度转为摄氏温度

    Args:
        f(float): Fahrenheit 华氏温度

    Return:
        float: Celsius 摄氏温度
    """
    return (f - 32) / 1.8


def c_f(c):
    """
    摄氏温度转为华氏温度

    Args:
        c(float): Celsius 摄氏温度

    Return:
        float: Fahrenheit 华氏温度
    """
    return c *1.8 + 32
