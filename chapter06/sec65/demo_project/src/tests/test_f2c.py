# coding = utf8
"""test demo_project"""

import os
import sys
import importlib
# from ...src.demo_package_author import tempe


class TestTempe:

    def setup(self):
        tests_path = os.path.split(__file__)[0]
        src_path = os.path.split(tests_path)[0]
        tempe_path = os.path.join(src_path, 'demo_package_author')
        sys.path.insert(0, tempe_path)
        # self.tempe = importlib.import_module('..demo_package_author.tempe', 'src')
        self.m = importlib.import_module('f2c')

    def test_tempe_fc(self):
        assert round(self.m.f_c(100), 1) == 37.8
        assert round(self.m.c_f(100), 1) == 212.0

    def teardown(self):
        pass
