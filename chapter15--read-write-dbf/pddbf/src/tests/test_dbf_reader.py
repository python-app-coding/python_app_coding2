# coding = utf8
import importlib
import os
import sys
import pandas as pd
import datetime as dt
import numpy as np


dft = pd.DataFrame(
    data={'serial_no': ['1010'+str(n) for n in range(1,5)],
          'en_name': ['Refrigerator', 'Washer', 'Stove', 'Ventilator'],
          'ch_name': ['冰箱', '洗衣机', '炉子', '通风机'],
          'price': [310.51, 420.35, 350, 210.4],
          'num': [100, 21, 333, 1234567],
          'shipping': [dt.datetime(2020, 3, 1, 1),
                       dt.datetime(2020, 3, 2, 1),
                       dt.datetime(2020, 3, 3, 0, 30),
                       dt.datetime(2020, 3, 4, 0, 0, 30),]}
)


class TestDbfreader:

    def setup(self):
        pydbfdir = os.path.abspath('../pddbf')
        sys.path.insert(0, pydbfdir)
        self.pydbf = importlib.import_module('pddbf')
        self.dfr = self.pydbf.read_dbf("dbf_with_cn.dbf")
        self.dfr = self.dfr.astype({'price': float, 'shipping': np.datetime64})

    def test_read_dbf1(self):
        assert all(self.dfr['serial_no'] == dft['serial_no'])

    def test_read_dbf2(self):
        assert all(self.dfr['en_name'] == dft['en_name'])

    def test_read_dbf2b(self):
        assert all(self.dfr['ch_name'] == dft['ch_name'])

    def test_read_dbf3(self):
        assert all(self.dfr['price'] == dft['price'])

    def test_read_dbf4(self):
        assert all(self.dfr['shipping'] == dft['shipping'])

    def teardown(self):
        sys.path.pop(0)
