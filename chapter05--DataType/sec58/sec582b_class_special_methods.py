# coding: utf8

import collections.abc as abc
import types


class MyClass:
    pass


class MyClass2:
    def __init__(self, x):
        self.__x = x

    def count(self, value):
        return self.__x.count(value)

    def index(self, value):
        return self.__x.index(value)

    def __len__(self):
        return len(self.__x)

    def __iter__(self):
        return iter(self.__x)

    def __reversed__(self):
        return reversed(self.__x)

    def __getitem__(self, item):
        return self.__x[item]

    # def __setitem__(self, key, value):
    #     self.__x[key] = value
    #
    # def __delitem__(self, key):
    #     del self.__x[key]

    def __contains__(self, item):
        return item in self.__x


class MyClass3(abc.Sequence):
    def __init__(self, x):
        self.__x = x

    def count(self, value):
        return self.__x.count(value)

    def index(self, value):
        return self.__x.index(value)

    def __len__(self):
        return len(self.__x)

    def __iter__(self):
        return iter(self.__x)

    def __reversed__(self):
        return reversed(self.__x)

    def __getitem__(self, item):
        return self.__x[item]

    # def __setitem__(self, key, value):
    #     self.__x[key] = value
    #
    # def __delitem__(self, key):
    #     del self.__x[key]

    def __contains__(self, item):
        return item in self.__x


def show_attrs(obj):
    pall = dir(obj)
    for lno, s in enumerate(pall):
        print(s, end=',  ')
        if (lno + 1) % 6 == 0:
            print("")
    print(f"\ntotal={len(pall)}")


# 在object中定义了23个特殊方法
print("dir(object):")
show_attrs(object)

# 自定义类中有26个特殊方法
# 多了__dict__, __module__, __weakref__
print("dir(MyClass2):")
show_attrs(MyClass2)

a, b = MyClass(), MyClass()
print(isinstance(a, abc.Sequence))

c = MyClass2([1, 2])
print(isinstance(c, abc.Sequence))
print(c.__len__(), len(c))

show_attrs(MyClass3)
print(isinstance(MyClass3([1, 2]), abc.Sequence))
