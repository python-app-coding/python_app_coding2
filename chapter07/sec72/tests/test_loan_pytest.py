# coding = utf8

"""
PyTest几种命令行指定测试集方式

【方式一】目录级运行
指定运行某一目录下所有测试集方式
命令格式：  pytest 目录名
> pytest tests/

【方式二】文件/模块级运行
即指定运行.py文件中的所有测试
命令格式： pytest 文件名.py
> pytest  xxxx.py

【方式三】运行测试类
命令格式：pytest 文件名.py::测试类
> pytest test_file::TestClass

【方式四】运行测试方法
命令格式：pytest 文件名.py::测试类::测试方法
> pytest test_file::TestClass::test_method
"""

from ..formulas import loan

# 使用绝对目录导入本文件相对位置模块
# import sys
# import os
# sys.path.append(os.path.dirname(__file__) + os.sep + '../formulas')
# import loan

import pytest


class Test1:

    def setup(self):
        self.input1 = (200, 30, 0.06, 1)
        self.result1_total_repay = 380.5
        self.input2 = (200, 30, 0.049, 2)
        self.result2_month_repay = 1.0614534412456103

    def test_repay(self):
        run_result = loan.repay(*self.input1)
        assert run_result.total_repay == self.result1_total_repay + 1
        run_result = loan.repay(*self.input2)
        assert run_result.month_repay[0] == self.result2_month_repay

    def teardown(self):
        print('test loan.repay finished!')


class Test2:

    # @pytest.mark.parametrize(
    #      'b, y, r, mode, result',
    #      [(200, 30, 0.06, 1, 380.5), (100, 30, 0.049, 1, 173.7041)]
    #      )
    # def test_repay_total_repay(self, b, y, r, mode, result):
    #     run_result = loan.repay(b, y, r, mode)
    #     assert round(run_result.total_repay, 2) == round(result, 2)

    @pytest.mark.parametrize('b,y,r,mode, result', [(200, 30, 0.049, 2, 1.0614534412456103)])
    def test_repay_month_repay(self, b, y, r, mode, result):
        run_result = loan.repay(b, y, r, mode)
        assert round(run_result.month_repay[0], 1) == round(result, 1)
