# coding = utf8

import collections.abc as abc
import sys


# 列表是可迭代对象，带有__iter__方法，是abc.Iterable的实例
a = [1, 2, 3]
print('__iter__' in dir(a))             # True
print(isinstance(a, abc.Iterable))      # True


# 可以由列表创建可迭代对象list_iterator
ai = iter([1, 2, 3])
print(type(ai))                         # list_iterator


# 字典的keys()方法返回一个可迭代对象， 占用内存很少
d = dict((chr(n), n) for n in range(97, 97+26))
print(d)                                # {'a': 97, 'b': 98, ..., 'z': 122}
dk = d.keys()
print(sys.getsizeof(dk))	            # 仅使用较少存储 40
print(sys.getsizeof(list(dk)))	        # 如果复制原有内容需要更多存储 264
