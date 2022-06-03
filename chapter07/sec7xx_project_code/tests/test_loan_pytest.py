# coding = utf8

# from ..formulas import loan
import sys
import os
sys.path.append(os.path.dirname(__file__) + os.sep + '../formulas')
# import loan
import pytest


class Test1:

    def setup(self):
        self.input1 = (200, 30, 0.06, 1)
        self.result1_total_repay = 380.51
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

    @pytest.mark.parametrize(
         'b, y, r, mode, result',
         [(200, 30, 0.06, 1, 380.5), (100, 30, 0.049, 1, 173.7041)]
         )
    def test_repay_total_repay(self, b, y, r, mode, result):
        run_result = loan.repay(b, y, r, mode)
        assert round(run_result.total_repay, 2) == round(result, 2)

    @pytest.mark.parametrize('b,y,r,mode, result', [(200, 30, 0.049, 2, 1.0614534412456103)])
    def test_repay_month_repay(self, b, y, r, mode, result):
        run_result = loan.repay(b, y, r, mode)
        assert round(run_result.month_repay[0], 1) == round(result, 1)
