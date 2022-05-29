# coding: utf8

import time


class WithObject:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()
        print(f"program start")
        pass

    def __exit__(self, type, value, trace):
        print("program end")
        print(f"use time:{time.time()-self.start:.4f}")


with WithObject():
    a = sum([x for x in range(1000000)])
