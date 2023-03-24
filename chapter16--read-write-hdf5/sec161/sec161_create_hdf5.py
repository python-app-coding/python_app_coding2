# coding = utf8

import numpy as np
import h5py as h5


def demo1_cteate_demo1_hdf5():
    """
    创建HDF5文件: demo1.hdf5
    [/]__ gp1: [dset1]
      |    |__ subgp11
      |__ gp2
      |     |__ subgp21
      |     |__ subgp22
      |__ gp3: [dset3]

    >>> h5f = h5.File('demo1.hdf5', 'w')
    >>> gp1 = h5f.create_group('gp1')
    >>> gp1.create_group('subgp11')
    >>> gp2 = h5f.create_group('gp2')
    >>> gp2.create_group('subgp21')
    >>> gp2.create_group('subgp22')
    >>> gp1.create_dataset('dset1')
    >>> h5f.create_dataset('/gp3/dset3')
    >>> h5f.close() 
    """


def create_demo2_hdf5():
    """
    创建HDF5文件demo2.hdf5, 并修改有关数据

    [/]__ : [dset1, dset2]
      |__ group1: [dset3]
      |__ group2: [dset4]

    # 准备存储到HDF5的字符、浮点、整数数据
    # 变长度字符型数据（str, Unicode字符串）
    >>> data1 = ['苹果apple', '橘子orange', '香蕉banana']

    # 固定长度字符型数据(|S6, ascii字节串)
    >>> data2 = np.array(['apple', 'orange', 'banana'], dtype='S6')

    # 浮点数类型(float64)
    >>> data3 = np.array([[ 0.3357,  1.408 , -0.5464], [ 2.188 ,  0.486 , -0.245 ],
    ...                   [-0.611 , -0.8223, -0.523 ]], dtype=np.float16)

    # 整数类型(int32)
    >>> data4 = np.array([[12, 23, 31], [31,  2, 84], [ 0, 74, 33]])

    # 创建HDF5文件
    >>> h5f = h5.File('demo2.hdf5', mode='w')

    # 使用变长字符串类型存储字符类型数据
    >>> dstr = h5.special_dtype(vlen=str)
    >>> dset1 = h5f.create_dataset('dset1', (3, ), dtype=dstr)
    >>> dset1[0:3] = data1[0:3]
    >>> dset1.attrs['name'] = 'fruit-1'
    >>> dset1[0]
    b'\xe8\x8b\xb9\xe6\x9e\x9capple'

    >>> [s.decode() for s in h5f['dset1']]
    ['苹果apple', '橘子orange', '香蕉banana']

    >>> h5f['dset1'].dtype
    dtype('O')

    # 使用固定长度类型存储字符串类型数据
    >>> h5f['dset2'] = data2
    >>> h5f['dset2'].attrs['name'] = 'fruit-2'

    >>> h5f['dset2'][:]
    array([b'apple', b'orange', b'banana'], dtype='|S6')

    # 管道符号'|'表示不需要标识字节顺序
    >>> print(h5f['dset2'].dtype)
    |S6

    # 使用create_dataset建立数据集，初始化时指定维度容量以及数据类型
    >>> d3 = h5f.create_dataset('/group1/dset3', (3, 3), dtype=np.float16)
    >>> d3[:] = data3
    >>> h5f['/group1/dset3'][:] = data3
    >>> h5f['/group1/dset3'][:]
    array([[ 0.3357,  1.408 , -0.5464],
           [ 2.188 ,  0.486 , -0.245 ],
           [-0.611 , -0.8223, -0.523 ]], dtype=float16)

    # 使用带有组名的数据集名称，可以直接建立组和数据集
    >>> h5f['/group2/dset4'] = data4
    >>> d4 = h5f['/group2/dset4']
    >>> d4[:]
    array([[12, 23, 31],
           [31,  2, 84],
           [ 0, 74, 33]])

    >>> print(h5f['/group2/dset4'].dtype)
    int32

    # 数据集的更名、删除、拷贝操作
    >>> h5f['/group2'].move('dset4', 'dset4new')	# 更改组内数据集名称
    >>> h5f['/group2'].keys()			            # 查看是否已经更改
    <KeysViewHDF5 ['dset4new']>

    >>> h5f['/group2'].copy('dset4new', 'dset4')	# 拷贝数据集dset4new到dset4
    >>> del h5f['/group2/dset4new']		            # 删除数据集dset4new

    >>> h5f.visit(print)
    dset1
    dset2
    group1
    group1/dset3
    group2
    group2/dset4

    # 引用不存在对象，会触发异常
    # >>> h5f['/group2/dset4new']
    # ...
    # KeyError: "Unable to open object (object 'dset4new' doesn't exist)"
    >>> g2 = h5f['/group2']
    >>> g2.get('dset4new')			# 使用get引用不存在对象，返回None
    >>> g2.get('dset4new', default=-1)		# 获取不存在的对象，设置default作为返回值
    -1

    >>> h5f.close()
    """


def create_demo3_hdf5():
    """
    create deom hdf5 file: [demo2.hdf5]
    /__ [dset1]
    |__ [dset2]
    |__ group1: [dset3]
    |__ group2: [dset4]
    |__ group3

    >>> h5f = h5.File('demo3.hdf5', 'w')
    >>> h5f.create_dataset('dset1', (3, ), dtype=h5.special_dtype(vlen=str))
    >>> h5f.create_dataset('dset2', (3, ), dtype='S6')
    >>> h5f.create_dataset('group1/dset3', (3, ))
    >>> h5f.create_dataset('group2/dset4', (3, ))
    >>> h5f.create_group('group3')
    >>> h5f.visit(print)
    >>> h5f.visititems(lambda name, obj: print(name, obj.shape) if isinstance(obj, h5.Dataset) else print(name))
    >>> h5f.close()
    """
