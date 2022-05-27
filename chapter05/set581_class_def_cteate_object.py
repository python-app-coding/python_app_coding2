# coding: utf8


class Foo:
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        print("Object is created!")
        return obj

    def __init__(self, x):
        self.x = x


foo = Foo(100)
print("foo.x = ", foo.x)


class Foo2:
    def __new__(cls, *args, **kwargs):  # 重新对象创建方法__new__
        print("object is created!")
        return None			            # 返回创建的对象

    def __init__(self, x):		        # 定义对象初始化方法
        print("Object is initialized!")  # 新增创建过程代码
        self.x = x			            # 设置对象属性


foo2 = Foo2(100)
print(type(foo2))
