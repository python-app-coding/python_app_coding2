# coding: utf8

import collections.abc as abc
import types


class MyClass:
    pass


class MyClass2:
    def __init__(self, x):
        self.__x = x

    def __getitem__(self, item):
        return self.__x[item]

    def __setitem__(self, key, value):
        self.__x[key] = value

    def __delitem__(self, key):
        del self.__x[key]

    def __contains__(self, item):
        return item in self.__x


# 在object中定义了23个特殊方法
print("dir(object):")
pall = dir(object)
for lno, s in enumerate(pall):
    print(s, end=', ')
    if (lno+1) % 6 == 0:
        print("")
print(f"\ntotal={len(pall)}")

# 自定义类中有26个特殊方法
# 多了__dict__, __module__, __weakref__
print("dir(MyClass):")
print(dir(MyClass), '\n', len(dir(MyClass)))

a, b = MyClass(), MyClass()
# print(a > b)
print(isinstance(a, abc.Hashable))
print(isinstance(a, abc.Sequence))
print(isinstance(MyClass2([1, 2]), abc.Sequence))
