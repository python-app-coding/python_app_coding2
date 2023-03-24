# coding = utf8

import numpy as np
import h5py as h5


def demo_modify_hdf5_data():
    """
    >>> npdata0 = np.array(['mongosteen', 'mongo', 'peach'], dtype='S10') # 改变字符类型为字节串
    >>> npdata1 = np.array()                                   # 改变维度
    >>> npdata2 = np.random.random_integers(100, 1000, (3, 3))            # 改变数据范围

    以读写方式打开HDF5文件：
    >>> h5f = h5.File('demo2.hdf5', 'r+')

    以切片赋值方式赋值，改变原数据集内容：
    >>> h5f['dset1'][0:2] = npdata0[0:2]
    >>> h5f['dset1'][:]
    ['mongosteen' 'mongo' '香蕉banana']

    改变数据集描述属性attr的内容：
    >>> h5f['dset1'].attrs['name'] = 'Fruit Store'
    >>> h5f['dset1'].attrs['name']
    Fruit Store

    删除组中的数据集，重新创建该数据集：
    >>> del h5f['/group1/dset3']
    >>> h5f['group1/dset3']
    KeyError: "Unable to open object (object 'group1' doesn't exist)"
    >>> h5f.create_dataset('/group1/dset3', data=npdata1, shape=(1, 9))
    >>> h5f['/group1/dset3'][:]
    [[ 0.24611495 -0.34292888 -1.29973889 -0.92347359 -2.91411261  1.08165077
       0.30797348  0.85759564  0.16389505]]

    重新赋值数据集所有数据：
    >>> h5f['/group2/dset4'][:] = npdata2[:]
    >>> h5f['/group2/dset4'][:]
    [[815 385 904]
     [810 632 796]
     [933 193 879]]

    检查组是否存在，如果不存在则创建新组（注意：使用get只检测组对象是否存在，不会创建组对象）：
    >>> h5f.require_group('group3')
    >>> h5f['group3']
    <HDF5 group "/group3" (0 members)>

    关闭HDF5文件对象：
    >>> h5f.close()
    """
