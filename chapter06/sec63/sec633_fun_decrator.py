# coding: utf8

import time


def print_time1(fun):
    def run():
        start = time.time()
        result = fun()
        print('time = {:.4f}'.format(time.time()-start))
        return result
    return run


@print_time1
def test(n=100000):
    return sum([i**2 for i in range(n)])


def print_time2(fun):
    def run(m):		# 在封装函数中加入参数
        start = time.time()
        result = fun(n=m)
        print('time = {:.4f}'.format(time.time()-start))
        return result
    return run


@print_time2
def test2(n=100000):
    return sum([x**2 for x in range(n)])


def printtime3(hint='time'):
    def dec(fun):
        def run(*args, **kwargs):
            start = time.time()
            result = fun(*args, **kwargs)
            print("{} = {:.4f}".format(hint, time.time()-start))
            return result
        return run
    return dec


@printtime3(hint='consume')
def test3(n=100000):
    return sum([x**2 for x in range(n)])


if __name__ == "__main__":
    print("run test:")
    test()

    print("run test2:")
    test2(10000)

    print("run test3:")
    test3(50000)
