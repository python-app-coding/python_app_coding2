# coding: utf8

"""
常量None的使用示例：
>>> b = None
>>> a = 1 if b else 0	    # None值被视为False
>>> b is None		        # 判断一个值是否是None
True
>>> b == None		        # 也可以使用比较值判断，但不推荐这样判断
True

>>> c1, c2 = Ellipsis, ...
>>> c1 == c2
True
>>> print([1, 2, ..., 100])
[1, 2, Ellipsis, 100]
"""