# coding = utf8

import time


class printtime_class:
    def __init__(self, hint='time'):
        self.hint = hint
    def __call__(self, fun):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = fun(*args, **kwargs)
            print('{}={:.4f}'.format(self.hint, time.time()-start))
            return result
        return wrapper


@printtime_class(hint='use class decorator, time')
def test_class_dec(n=100000):
    return sum([x**2 for x in range(n)])


class TestDecMethod:
    @printtime_class('used in class method, time')
    def test_method(self, n=100000):
        return sum([x**2 for x in range(n)])


if __name__ == "__main__":
    print("run test_class_dec:")
    test_class_dec()

    print("run test_method:")
    TestDecMethod().test_method(10000)
