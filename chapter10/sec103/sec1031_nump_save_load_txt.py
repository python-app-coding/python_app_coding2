# coding = utf8

import numpy as np


def demo1_savetxt():
    """
    #使用empty方法生成多维数组，数据格式为16位浮点数
    # >>> a1 = np.empty((3, 3), dtype=np.float16)
    >>> a1 = np.array([[1.224e+00, 1.696e+03, 2.591e-02],
    ...                [5.949e-05, 1.971e+03, 2.603e-02],
    ...                [9.868e-01, 1.466e+03, 3.674e-03]], dtype=np.float16)

    # 使用np.savetxt保存数据到文本文件, 保留6为小数
    >>> np.savetxt('temp_np_savetxt.txt', a1, fmt='%.6f', delimiter=',')

    # 通过open方法读出打印文件内容
    >>> with open('temp_np_savetxt.txt') as fp:
    ...     for line in fp.readlines():
    ...         print(line)
    1.223633,1696.000000,0.025909
    0.000059,1971.000000,0.026031
    0.986816,1466.000000,0.003674
    """


def demo2_loadtxt():
    """
    # 使用np.loadtxt读出文件到numpy数组，数据格式为np.float（64位浮点数）
    >>> a2 = np.loadtxt('temp_np_savetxt.txt', dtype=np.float32, delimiter=',')
    >>> a2
    array([[1.223633e+00, 1.696000e+03, 2.590900e-02],
           [5.900000e-05, 1.971000e+03, 2.603100e-02],
           [9.868160e-01, 1.466000e+03, 3.674000e-03]], dtype=float32)
    """
