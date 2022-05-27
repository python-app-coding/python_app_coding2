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
