# coding = utf8

import os
from tools import add, path, tempe


if __name__ == '__main__':
    print("demo add.add2: add.add2(100, 200) = {}".format(add.add2(100, 200)))
    print("demo add.add: add.add(100, 200, 300) = {}".format(add.add(100, 200, 300)))
    print("demo path: path.abspath('.') = {}".format(path.abspath('.')))
    print("demo tempe: tempe.f_c(100) = {}".format(tempe.f_c(100)))
    print("demo tempe: tempe.c_f(100) = {}".format(tempe.c_f(100)))
