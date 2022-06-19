# coding = utf8

import h5py as h5


def show_groups(h5file):
    """
    遍历打印HDF5文件h5file中的组对象

    >>> show_groups('demo_traverse.hdf5')
    Groups in demo_traverse.hdf5:
    <HDF5 group "/group1" (1 members)>
    <HDF5 group "/group2" (1 members)>
    <HDF5 group "/group3" (0 members)>
    """

    h5f = h5.File(h5file, 'r')
    print("Groups in {}:".format(h5file))
    h5f.visititems(lambda name, obj: print(obj) if isinstance(obj, h5.Group) else None)
    h5f.close()


def show_datasets(h5file):
    """
    遍历打印HDF5文件h5file中的数据集

    >>> show_datasets('demo_traverse.hdf5')
    Datasets in demo_traverse.hdf5:
    <HDF5 dataset "dset1": shape (3,), type "|O">
    <HDF5 dataset "dset2": shape (3,), type "|S6">
    <HDF5 dataset "dset3": shape (3,), type "<f4">
    <HDF5 dataset "dset4": shape (3,), type "<f4">
    """

    h5f = h5.File(h5file, 'r')
    print("Datasets in {}:".format(h5file))
    h5f.visititems(lambda name, obj: print(obj) if isinstance(obj, h5.Dataset) else None)
    h5f.close()

# 显示每个检索到的对象的类型
def show_objects(h5file, h5dtype=h5.Group):
    """
    遍历HDF5文件h5file，保存其中的类型为h5dtype的所有对象
    ：param h5file: str HDF5文件名称
    ：param h5dtype: HDF5数据对象，包括h5py.File, h5py.Group, h5py.Dataset
    : return list: 遍历对象的列表

    >>> objlist = show_objects('demo_traverse.hdf5')
    >>> objlist
    ['group1', 'group2', 'group3']

    >>> objlist = show_objects('demo_traverse.hdf5', h5.Dataset)
    >>> objlist
    ['dset1', 'dset2', 'group1/dset3', 'group2/dset4']
    """

    h5f = h5.File(h5file, 'r')
    objlist = []
    h5f.visititems(lambda name, obj: objlist.append(name) if isinstance(obj, h5dtype) else None)
    h5f.close()
    return objlist
