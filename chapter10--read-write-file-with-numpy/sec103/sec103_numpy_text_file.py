# coding: utf8

import numpy as np


def demo_numpy_savetxt():
    """
    demo numpy function savetxt to write numpy ndarray to text file

    """

    tempfile = "temp_text.txt"
    data = np.array([np.array(range(1, 10))*j for j in range(1, 10)])
    print(data)
    np.savetxt(fname=tempfile, X=data, fmt="%3u",
               delimiter=",",
               newline="\n", header="9X9 multiplication table",
               footer="--- table end ---", comments="#", encoding="utf8")

    data1 = np.empty((3, 3), dtype=np.float16)
    print(data1)
    np.savetxt("demo_np_savetxt.txt", data1, fmt="%.10f", delimiter=",")


def demo_numpy_loadtxt():
    """
    use numpy function to read text data to ndarray

    """
    tempfile = "temp_text.txt"
    data = np.loadtxt(fname=tempfile, dtype=np.uint8, delimiter=",",
                      comments="#", encoding="utf8")
    print(data, "\n", data.shape)

    data2 = np.loadtxt("demo_np_savetxt.txt", dtype=np.float_, delimiter=",")
    print(data2)


if __name__ == "__main__":
    demo_numpy_savetxt()
    demo_numpy_loadtxt()
