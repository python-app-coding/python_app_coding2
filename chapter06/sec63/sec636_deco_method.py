# coding = utf8


def dec_fun(fun):
    def wrapper(obj, *args, **kwargs):
        result = fun(obj, *args, **kwargs)
        result = 0 if result < 0 else result+1000
        return result
    return wrapper


# 装饰对象方法
class UserClass:
    # 装饰对象方法
    @dec_fun
    def m1(self, x):
        return x*2

    # 装饰类方法
    @classmethod
    @dec_fun
    def m2(cls, x):
        return x**2

    # 装饰静态方法
    @staticmethod
    @dec_fun
    def m3(x):
        return x**3


uc = UserClass()
print(uc.m1(-3), UserClass.m2(3), UserClass.m3(3))
