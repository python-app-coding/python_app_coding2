# coding: utf8


class Foo:
    p = 100

    def __init__(self, x=1):
        self.x = x
        print("object.x = {}".format(self.x))

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        print("Object is created!")
        return obj

    def m1(self, y):
        print(self.x, y)

    @classmethod
    def m2(cls, y):
        print(cls.p, y)

    @staticmethod
    def m3(z):
        print(Foo.p,z)


if __name__ == "__main__":
    foo = Foo(10)
    foo.m1(20)
    Foo.m2(20)
    Foo().m2(30)
    Foo.m3(40)
    Foo().m3(50)
