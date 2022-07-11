=========================================
Pandas DataFrame and DBF data Conversion
=========================================

pddbf named from Pandas.DataFrame and DBF data conversion tool.
By pddbf interface functions or Classes, You can read DBF file to DataFrame,
or write DataFrame to DBF file.

However, Only some common types (C, N, B, D, F, L, I for DBf) can be supported.
Meanwhile, use a types-map from DataFrame types to DBF common types to write DataFrame to DBF file.
When no corresponding type used in DBF, convert DataFrame column type to string by str() to DBF C type.

------------------
1. Api Functions
------------------

Module Methods of pddbf.pddbf
-----------------------------

read_dbf(dbffile): read DBF file data to DataFrame. 读取DBF文件数据为DataFrame

to_dbf(df, dbffile): Celsius to Fahrenheit 将DataFrame写为DBF文件

Classes in pddbf
----------------

class Dbf(builtins.object)
 |  A class used to read and write DBF file，its property data is DataFrame
 |
 |  data: DataFrame, data read from dbf file
 |
 |  open(self, filename: str = '')
 |      open a DBF file, prework for load method
 |      :parameters
 |      filename: str, file name to open
 |
 |  close()
 |      close dbf file
 |
 |  fetch(self, start=1, count=10)
 |      read DBF file data from the file opened in use
 |
 |      :parameters
 |      start: int, positive, start record serial number to read from DBF file
 |      count: int, positive, record count to read from DBF file
 |
 |  to_csv(self, csvfile='temp.csv', sep=',')
 |      write data to csv file
 |
 |      :parameters
 |      csvfile: str. 'temp.csv'( default). file name to write.
 |      sep: str. ','( default).  length is 1. charater used to seperate field data in record line.
 |
 |  to_dbf(self, dbffile='temp.dbf_bak')
 |      write data to DBF file
 |
 |      :parameters
 |      dbffile: str. 'temp.dbf_bak'( default). file name to write.

class DbfReader(builtins.object)
 |  Methods defined:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  close(self)
 |
 |  fetchall(self)
 |
 |  fetchmany(self, start=1, count=10)
 |      :param start first record no in dbf table, record no is range(1, len(dbf)+1)
 |      :param count record number fetched from dbf table, fetch record: start,...,start+count-1
 |
 |  open(self, filename=None)
 |      open dbf and load 10 rows of records to data
 |      :param filename: dbf file name
 |      :return: None
 |
 |  parse_header(self)
 |
 |  parse_record(self, fp)
 |      convert data from dBase types to pandas types:
 |          dBase  type: C, V, N, F, D, L, I, B, O, T, @
 |          pandas type: str, int64, decimal.Decimal, np.date, datetime, bool, np.float64
 |
 |      parse dbf data to pandas:
 |          C, V: decode to str by bytes.decode
 |          N, F: decode to str by bytes.decode
 |                parse to Decimal if decimal > 0 else to int
 |             I: decode to integer by unpack
 |             D: decode to str by bytes.decode
 |                parse date by datetime.date(year, month, day)
 |          T, @: decode to datetime by unpack 2 long integers
 |                parse to date and time by get_date_by_days and get_time_by_compound_value
 |          B, O: decode to float64 by unpack
 |             L: decode to str by bytes.decode
 |                parse to True if 'YyTt' else False
 |         other: remain to binary byte string, including(G,P,M,Y,...)
 |
 |      :param fp: file handle
 |      :return: list with field-data


class DbfWriter(builtins.object)
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  to_dbf(self, df, dbffile='tempdbf.dbf')
 |      covert DataFrame to dBase file
 |  get_field_spec_from_dataframe(df)
 |      use some strategies to set field type,size,decimal
 |  write_dbf_header(fp, field_spec, data)
 |      analyze and write header_info (including: file-info, field-inof, terminator, extended 263 bytes)
 |  write_dbf_records(fp, field_spec, df)
 |      write DataFrame rows to Dbf records


------------
2.How to Run
------------

install
-------
> pip install pddbf_package_wangxichang

import
-------
>>> from pddbf import read_dbf, to_dbf
>>> df = pd.DataFrame({'a': range(3), 'b': list('xyz')})
>>> to_dbf(df, 'demo_write.dbf')
>>> df2 = read_dbf('demo_write.dbf')
>>> df2


---------------------
3. Project Structure
---------------------
pddbf
    src
        pddbf
            pddbf.py
            dbfreader.py
            dfbwriter.py
        tests
            test_dbf_reader.py
            test_dbf_writer.py
    docs
        index.rst

-------
4. FAQ
-------

- [1] What is DataFrame?

a primary data structure of pandas
2D table with index, columns

- [2] How to install pddbf?

pddbf have uploaded PyPI, please use pip install pddbf to install

- [3] How to read DBF by pddbf?

  mode1:

 >>> import pddbf
 >>> df = pddbf.read_dbf(dbffilename)

  mode2:

 >>> from pddbf import *
 >>> df = read_dbf(dbffilename)

- [4] How to write DataFrame to DBF file by pddbf?

 >>> df = pddbf.to_dbf(df=dataframe_name, dbffile=dbf_file_name)
