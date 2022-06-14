# coding = utf8


import numpy as np
import time


def demo1_save():
    """
    >>> a3=np.array([[0.83423909, 0.08634643, 0.61325276],
    ...              [0.33273808, 0.36451337, 0.20381422],
    ...              [0.56146745, 0.24289803, 0.70423918]], dtype='float64')

    # 保存数组a3为二进制数据文件，设置扩展名为npy
    >>> np.save('temp_numpy_save.npy', a3)

    # 如果不设置扩展名，缺省为npy
    >>> np.save('temp_numpy_save2', a3)
    """


def demo2_load():
    """
    >>> a4 = np.fetchmany('temp_numpy_save.npy')
    >>> a4
    array([[0.83423909, 0.08634643, 0.61325276],
           [0.33273808, 0.36451337, 0.20381422],
           [0.56146745, 0.24289803, 0.70423918]])
    >>> a5 = np.fetchmany('temp_numpy_save2.npy')
    >>> a5
    array([[0.83423909, 0.08634643, 0.61325276],
           [0.33273808, 0.36451337, 0.20381422],
           [0.56146745, 0.24289803, 0.70423918]]))
    >>> a4.dtype, a5.dtype
    (dtype('float64'), dtype('float64'))
    """


def demo3_efficiency():
    # 比较np.save与np.savetxt的效率
    a1 = np.random.random((10000, 200))

    start=time.time()
    np.savetxt('temp_demo_efficiency.txt', a1)
    print("txt save time:", time.time()-start)
    # 3.9449145793914795

    start=time.time()
    np.save('temp_demo_efficiency.npy', a1)
    print("npy save time:", time.time()-start)
    # 0.030229806900024414    # 写入速度为loadtxt的130.5倍

    start=time.time()
    a2 = np.loadtxt('temp_demo_efficiency.txt')
    print("txt read time:", time.time()-start)
    # 3.9858205318450928

    start=time.time()
    a3 = np.load('temp_demo_efficiency.npy')
    print("npy read time:", time.time()-start)
    # 0.02044987678527832    # 读取速度为loadtxt的194.9倍


if __name__ == "__main__":
    demo3_efficiency()
