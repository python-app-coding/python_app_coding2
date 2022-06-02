# coding = utf8

import collections.abc as abc

r = range(3, 10)
print(isinstance(r, abc.Iterable))		# r是可迭代对象，可以通过iter转换为迭代器 True
print(isinstance(r, abc.Iterator))		# r不是迭代器，不支持使用next进行迭代, False
print(isinstance(r, abc.Sequence))		# r是序列，支持下标方式访问取值, True
print(r[1])                             # 4
print(list(r))			# 使用list可以转换为一个列表 [3, 4, 5, 6, 7, 6, 9]
for i in range(1, 10, 2):	         # 作为可迭代对象，可以使用for循环进行遍历
    print(i, ' ', end='')
# 1 3 5 7 9
