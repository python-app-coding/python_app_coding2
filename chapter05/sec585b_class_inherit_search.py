# coding: utf8


class A:
    def m1(self):
        print('A-method')


class B(A):
    def m1(self):
        print('B-method')


class C:
    def m1(self):
        print('C-method')


class D(C, B, A):
    pass


D().m1()
print(D.__mro__)

# print(help(D.__mro__))


class E(A, B):
    pass
