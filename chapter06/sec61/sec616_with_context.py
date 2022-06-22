# coding: utf8

import importlib as pb


class WithClass:
    def __init__(self):
        self.time = pb.import_module('time')
        self.start = None

    def __enter__(self):
        self.start = self.time.time()
        print(f"program start")
        pass

    def __exit__(self, etype, evalue, traceback):
        if etype:
            print(etype, evalue)
            # print(traceback.print_exception(etype, evalue, traceback))
        print("program end")
        print(f"use time:{self.time.time()-self.start:.4f}")
        return True


if __name__ == '__main__':
    with WithClass():
        print(sum([x for x in range(1000000)]))

    with WithClass():
        1 / 0
        print(sum([x for x in range(1000000)]))
