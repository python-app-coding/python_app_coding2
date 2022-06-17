# coding = utf8

import numpy as np
import h5py as h5


# 准备存储到HDF5的字符、浮点、整数数据
# 变长度字符型数据（str, Unicode字符串）
data1 = ['苹果apple', '橘子orange', '香蕉banana']
# 固定长度字符型数据(|S6, ascii字节串)
data2 = np.array(['apple', 'orange', 'banana'], dtype='S6')
# 浮点数类型(float64)
data3 = np.random.randn(3, 3)                                   
# 整数类型(int32)
data4 = np.random.randint(0, 100, (3, 3))

print(data1, '\n', data2, '\n', data3, '\n', data4)

# 创建一个HDF5文件
h5file = h5.File('temp_hdf5.h5', mode='w')

# 使用变长字符串类型存储字符类型数据
dstr = h5.special_dtype(vlen=str)
h5file.create_dataset('dset1', (3, ), dtype=dstr)
h5file['dset1'][0:3] = data1[0:3]
h5file['dset1'].attrs['name'] = 'fruit-1'

print("\n--- ref dset1")
print("h5file['dset1'][:]: ", h5file['dset1'][:])
print("decode: ", [s.decode() for s in h5file['dset1']])
# ['苹果apple' '橘子orange' '香蕉banana']
print("dtype: ", h5file['dset1'].dtype)
# object

# 使用固定长度类型存储字符串类型数据
h5file['dset2'] = data2
h5file['dset2'].attrs['name'] = 'fruit-2'

print("\n--- ref dset2")
print(h5file['dset2'])
# [b'apple' b'orange' b'banana']
print(h5file['dset2'].dtype)
# |S6       	# 管道符号'|'表示不需要标识字节顺序

# 使用create_dataset建立数据集，初始化时指定维度容量以及数据类型
d3 = h5file.create_dataset('/group1/dset3', (3, 3), dtype=np.float16)
d3[:] = data3
# h5file['/group1/dset3'][:] = data3

print("\n--- ref dset3")
print(h5file['/group1/dset3'][:])
print(np.array(h5file['/group1/dset3']))
# [[ 1.076  -0.2382  1.636 ]
#  [ 0.2551  1.253  -1.953 ]
#  [-0.7427  1.539  -0.945 ]]

# 使用带有组名的数据集名称，可以直接建立组和数据集
h5file['/group2/dset4'] = data4
d4 = h5file['/group2/dset4']

print("\n--- ref dset4")
print("d4: ", d4)
print("d4.shape= ", d4.shape)
print([v for v in d4])
# [[42 91  9]
#  [ 6 34  3]
#  [ 5  0 31]]

print(h5file['/group2/dset4'].dtype)
# int32

h5file.close()
