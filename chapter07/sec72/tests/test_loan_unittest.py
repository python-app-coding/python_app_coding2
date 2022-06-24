# coding: utf8

import unittest
from ..formulas import loan


class TestRepayLoan(unittest.TestCase):

    def setUp(self) -> None:
        self.test_input1 = (200, 30, 0.06, 1)
        self.test_result1_total_repay = 380.5

    def test_repay(self):
        result = loan.repay(*self.test_input1)
        self.assertEqual(round(result.total_repay, 1),
                         self.test_result1_total_repay,
                         "200wan, 30years, 0.06rate")

    def tearDown(self) -> None:
        print('tests house_loan is finished!')


if __name__ == '__main__':
    unittest.main()
