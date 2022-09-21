# coding = utf8

import importlib
import os.path
import sys


class TestHello:

    def setup(self):
        source_path = '../foo'
        sys.path.insert(0, os.path.abspath(source_path))
        self.hello = importlib.import_module("hello")

    def test_hello(self):
        assert self.hello.hello() is None
