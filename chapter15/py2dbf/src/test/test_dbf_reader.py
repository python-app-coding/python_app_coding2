# coding = utf8
import importlib
import os
import sys



class TestDbf():

    def setup(self):
        dbfdir = os.path.abspath('../py2dbf')
        sys.path.insert(0, dbfdir)
        self.dbf = importlib.import_module('dbf')

    def test_read_dbf(self):
        df = self.dbf.read_dbf("demo.dbf")
        print(df)
        # assert df[0] == 1
