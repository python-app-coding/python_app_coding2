# coding = utf8

import collections.abc as abc
import sys

a = [1, 2, 3]
print('__iter__' in dir(a))             # True
print(isinstance(a, abc.Iterable))      # True

ai = iter([1, 2, 3])
print(type(ai))         # list_iterator

d = dict((chr(n), n) for n in range(97, 97+26))
print(d)        # {'a': 97, 'b': 98, ..., 'z': 122}
dk = d.keys()

print(sys.getsizeof(dk))	      # 仅使用较少存储 40
print(sys.getsizeof(list(dk)))	  # 如果复制原有内容需要更多存储 264
