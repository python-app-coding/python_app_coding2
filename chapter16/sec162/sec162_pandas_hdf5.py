# coding = utf8


import pandas as pd
import datetime as dt


sr = pd.Series(
    data=['程柳青', '窦建军', '张梦想'],
    index=[dt.datetime(2010, 1, 1)+pd.DateOffset(i) for i in range(3)])

df = pd.DataFrame(
    data = {
        'id': ['001', '002', '003'],
        'name': ['程柳青', '窦建军', '张梦想'],
        'math': [100, 90, 92],
        'art': [77.50, 98.20, 87.77],
        'birth': [dt.datetime(2001, 3, 5), dt.datetime(1998, 2, 1), dt.datetime(2002, 12, 15)],
        'pass': [True, False, True]
    }
)

hdf5file ='demo_hdfstore.hdf5'


def demo1_data():
    """
    # pandas 数据集
    >>> sr
    2010-01-01    程柳青
    2010-01-02    窦建军
    2010-01-03    张梦想
    dtype: object

    >>> sr.index
    DatetimeIndex(['2010-01-01', '2010-01-02', '2010-01-03'], dtype='datetime64[ns]', freq=None)

    >>> df
        id name  math    art       birth   pass
    0  001  程柳青   100  77.50  2001-03-05   True
    1  002  窦建军    90  98.20  1998-02-01  False
    2  003  张梦想    92  87.77  2002-12-15   True
    """


def demo2_h5store_create_hd5_file():
    """
    # 注意：有些类型不能序列化，如datetime.date

     >>> h5store = pd.HDFStore(hdf5file, mode='w')
     >>> h5store.put('group1/sr', sr)                   # 使用put方法创建，缺省格式为series
     >>> h5store['group2/df'] = df                      # 直接赋值创建, 缺省格式为frame
     >>> h5store.put('sr', sr, format='table')          # 使用put创建table格式数据集
     >>> h5store.put('df', df, format='table')          # 使用put创建table格式数据集
     >>> h5store['group5/group51/group511/df'] = df     # 在多层目录中直接创建数据集
     >>> h5store.close()
    """


def demo3_keys_pandas_type():
    """
    >>> h5store = pd.HDFStore(hdf5file)

    # 列出HDF5中数据对象情况
    >>> h5store.keys()
    ['/df', '/sr', '/group5/group51/group511/df', '/group2/df', '/group1/sr']

    # 查看数据集格式
    >>> h5store.root.sr._v_attrs.pandas_type
    'series_table'
    >>> h5store.root.df._v_attrs.pandas_type
    'frame_table'
    >>> h5store.root.group1.sr._v_attrs.pandas_type
    'series'
    >>> h5store.root.group2.df._v_attrs.pandas_type
    'frame'

     >>> h5store.close()
    """


def demo4_walk():
    """
    >>> h5store = pd.HDFStore(hdf5file)

    >>> for group, subgroups, objects in h5store.walk():
    ...     print(group, subgroups, objects)   	# 各组的组名、子组名列表、对象名列表
     ['group1', 'group2', 'group5'] ['df', 'sr']
    /group1 [] ['sr']
    /group2 [] ['df']
    /group5 ['group51'] []
    /group5/group51 ['group511'] []
    /group5/group51/group511 [] ['df']

    >>> for group, subgroups, objects in h5store.walk(where='/group5'):
    ...     print(group, subgroups, objects)   	# 各组的组名、子组名列表、对象名列表
    /group5 ['group51'] []
    /group5/group51 ['group511'] []
    /group5/group51/group511 [] ['df']

    >>> h5store.close()
    """


def demo5_():
    """
    >>> h5store = pd.HDFStore(hdf5file)

    # -- fixed格式数据集不允许添加数据
    #  >>> h5store.append('group1/sr', sr)
    ValueError: Can only append to Tables

    # -- table格式数据集允许添加数据
    >>> h5store.append('sr', sr)
    >>> h5store['sr']
    2010-01-01    程柳青
    2010-01-02    窦建军
    2010-01-03    张梦想
    2010-01-01    程柳青
    2010-01-02    窦建军
    2010-01-03    张梦想
    dtype: object

    >>> h5store.close()
    """


def demo6_():
    """
    >>> h5store = pd.HDFStore(hdf5file, mode='a')

    # 使用put方法生成table格式数据集(覆盖已有数据集)
    >>> h5store.put('sr2', sr, format='table')          # 使用put创建table格式数据集
    >>> h5store.put('df2', df, format='table')          # 使用put创建table格式数据集

    >>> h5store['sr2'][:]
    2010-01-01    程柳青
    2010-01-02    窦建军
    2010-01-03    张梦想
    dtype: object

    >>> h5store['df2'][:]
        id name  math    art      birth   pass
    0  001  程柳青   100  77.50 2001-03-05   True
    1  002  窦建军    90  98.20 1998-02-01  False
    2  003  张梦想    92  87.77 2002-12-15   True

    # 查看格式
    >>> h5store.root.sr2._v_attrs.pandas_type
    'series_table'
    >>> h5store.root.df2._v_attrs.pandas_type
    'frame_table'

    # 以append模式创建HDF5数据集, 缺省模式为table格式
    >>> h5store.append('sr2', sr)
    >>> h5store.append('df2', df)

    # 两次添加的数据情况
    >>> h5store['sr2'][:]
    2010-01-01    程柳青
    2010-01-02    窦建军
    2010-01-03    张梦想
    2010-01-01    程柳青
    2010-01-02    窦建军
    2010-01-03    张梦想
    dtype: object

    >>> h5store['df2'][:]
        id name  math    art      birth   pass
    0  001  程柳青   100  77.50 2001-03-05   True
    1  002  窦建军    90  98.20 1998-02-01  False
    2  003  张梦想    92  87.77 2002-12-15   True
    0  001  程柳青   100  77.50 2001-03-05   True
    1  002  窦建军    90  98.20 1998-02-01  False
    2  003  张梦想    92  87.77 2002-12-15   True

    >>> h5store.close()
    """


def demo7_():
    """
    >>> h5store = pd.HDFStore(hdf5file)
    >>> h5store.close()

    # 将DataFrame对象写为HDF5数据集，并指定可查询列
    >>> df.to_hdf(h5store, key='df3', data_columns=['math', 'art'], mode='w', format='table')

    >>> h5store = pd.HDFStore(hdf5file)

    >>> h5store['df3'].query('index==1')
        id name  math   art      birth   pass
    1  002  窦建军    90  98.2 1998-02-01  False

    >>> h5store['df3'].query('name=="程柳青"')
        id name  math   art      birth  pass
    0  001  程柳青   100  77.5 2001-03-05  True

    >>> h5store.select('df3', where=["index > 1 & columns in ['id']"])
        id
    2  003

    # 调用data_columns中定义的列
    >>> h5store.select('df3', where=["math > 90"])
        id name  math    art      birth  pass
    0  001  程柳青   100  77.50 2001-03-05  True
    2  003  张梦想    92  87.77 2002-12-15  True

    # 从HDFStore对象查询
    >>> pd.read_hdf(h5store, key='df3', where=['art >= 80'])
        id name  math    art      birth   pass
    1  002  窦建军    90  98.20 1998-02-01  False
    2  003  张梦想    92  87.77 2002-12-15   True

    # 指定HDF5文件名查询(需要先关闭hdfstore对象，除非是以只读方式打开)
    >>> h5store.close()
    >>> pd.read_hdf(hdf5file, key='df3', where=['art >= 80', 'math > 90'], columns=['name', 'math', 'art'])
      name  math    art
    2  张梦想    92  87.77
    """


def demo8_():
    """
    >>> h5store = pd.HDFStore(hdf5file)

    # 调用drop方法删除一个数据列
    >>> h5store['df3'] = h5store['df3'].drop(labels=['pass'], axis=1)
    >>> h5store.flush()	# 保存
    >>> h5store['df3']	# 查看删除情况
        id name  math    art      birth
    0  001  程柳青   100  77.50 2001-03-05
    1  002  窦建军    90  98.20 1998-02-01
    2  003  张梦想    92  87.77 2002-12-15

    # 设置axis=0，按照行号删除行
    >>> h5store['df3'] = h5store['df3'].drop(labels=[0, 2], axis=0)
    >>> h5store.flush()
    >>> h5store['df3']
        id name  math   art      birth
    1  002  窦建军    90  98.2 1998-02-01

    # 删除数据集
    >>> h5store['sr'] = pd.Series(list('abc'))
    >>> h5store['sr']
    0    a
    1    b
    2    c
    dtype: object

    >>> h5store.remove(key='sr')

    # 删除后不能再引用
    # >>> h5store['sr']
    # KeyError: 'No object named group3/sr in the file'

    >>> h5store.close()
    """
