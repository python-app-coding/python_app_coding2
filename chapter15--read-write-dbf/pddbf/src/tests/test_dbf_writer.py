# coding: utf

import os
import sys
import pandas as pd
import importlib
import numpy as np
import faker
import time


class TestDbfwriter:

    def setup(self):
        dbfdir = os.path.abspath('../pddbf')
        sys.path.insert(0, dbfdir)
        pydbf = importlib.import_module('pddbf')

        fk = faker.Faker('zh_cn')
        record_num = 100000
        self.dffaker = pd.DataFrame(
            data={
                'id': list(range(record_num)),
                'name': [fk.name() for _ in range(record_num)],
                'age': [fk.random.randint(12, 30) for _ in range(record_num)],
                'weight': [fk.random.random() for _ in range(record_num)],
                'addr': [fk.address() for _ in range(record_num)],
                'date': [fk.date_this_decade() for _ in range(record_num)]
            }
        )

        st = time.time()
        tempfile = os.path.join(dbfdir, 'temp_test_10w.dbf')
        pydbf.to_dbf(self.dffaker, tempfile)
        self.write_time = time.time()-st

        st = time.time()
        self.dfr = self.pydbf.read_dbf(tempfile)
        self.dfr = self.dfr.astype({'date': np.datetime64})
        self.read_time = time.time() - st

    def test_write_dbf0(self):
        assert self.write_time < 5
        assert self.read_time < 3

    def test_read_dbf1(self):
        assert all(self.dfr['id'] == self.dffaker['id'])

    def test_read_dbf2(self):
        assert all(self.dfr['name'] == self.dffaker['name'])

    def test_read_dbf2b(self):
        assert all(self.dfr['age'] == self.dffaker['age'])

    def test_read_dbf3(self):
        assert all(self.dfr['addr'] == self.dffaker['addr'])

    def test_read_dbf4(self):
        assert all(self.dfr['date'] == self.dffaker['date'])
