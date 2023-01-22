# coding = utf8

import h5py as h5


def demo_traverse_dict_methods():
    """
    >>> h5f = h5.File('demo_traverse.hdf5', 'r')

    # 使用items搜索组中数据对象
    >>> for item in h5f.items():
    ...     print(item)
    ('dset1', <HDF5 dataset "dset1": shape (3,), type "|O">)
    ('dset2', <HDF5 dataset "dset2": shape (3,), type "|S6">)
    ('group1', <HDF5 group "/group1" (1 members)>)
    ('group2', <HDF5 group "/group2" (1 members)>)
    ('group3', <HDF5 group "/group3" (0 members)>)

    # 使用keys以键名称检索键：
    >>> for item in h5f.keys():
    ...     print(item)
    dset1
    dset2
    group1
    group2
    group3

    # 以value方式检索值：
    >>> for item in h5f.values():
    ...     print(item)
    <HDF5 dataset "dset1": shape (3,), type "|O">
    <HDF5 dataset "dset2": shape (3,), type "|S6">
    <HDF5 group "/group1" (1 members)>
    <HDF5 group "/group2" (1 members)>
    <HDF5 group "/group3" (0 members)>

    >>> h5f.close()
    """


def demo_traverse_visit():
    """
    >>> h5f = h5.File('demo_traverse.hdf5', 'r')

    # 将打印函数print传递给visit，可以打印处每个检索到的对象
    >>> h5f.visit(print)
    dset1
    dset2
    group1
    group1/dset3
    group2
    group2/dset4
    group3

    # 将列表方法append传递给vist，可以预定的列表中收集遍历的对象
    >>> objlist = []
    >>> h5f.visit(objlist.append)
    >>> objlist
    ['dset1', 'dset2', 'group1', 'group1/dset3', 'group2', 'group2/dset4', 'group3']

    >>> objlist = []
    >>> h5f['group1'].visit(objlist.append)
    >>> objlist
    ['dset3']

    >>> h5f.close()
    """


def demo_traverse_visititems():
    """
    >>> h5f = h5.File('demo_traverse.hdf5', 'r')

    # 让回调函数接受两个参数，将对象名称和对象组成一个元组，保存到收集列表
    >>> objlist = []
    >>> fun2 = lambda x, y: objlist.append((x, y))
    >>> h5f.visititems(fun2)
    >>> print('\\n'.join([str(tp) for tp in objlist]))
    ('dset1', <HDF5 dataset "dset1": shape (3,), type "|O">)
    ('dset2', <HDF5 dataset "dset2": shape (3,), type "|S6">)
    ('group1', <HDF5 group "/group1" (1 members)>)
    ('group1/dset3', <HDF5 dataset "dset3": shape (3,), type "<f4">)
    ('group2', <HDF5 group "/group2" (1 members)>)
    ('group2/dset4', <HDF5 dataset "dset4": shape (3,), type "<f4">)
    ('group3', <HDF5 group "/group3" (0 members)>)

    # 在回调函数中检测名称，返回具有特定性质的对象
    >>> def fun3(key, obj):
    ...     if obj.attrs.get('name') == 'fruit-2':
    ...            return obj
    >>> result = h5f.visititems(fun3)
    >>> result
    [b'apple' b'orange' b'banana']

    >>> h5f.close()
    """
