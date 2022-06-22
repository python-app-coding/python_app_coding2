# coding: utf8


import itertools as itl

# 无穷计数器
c = itl.count(0, 10)	# 从0开始，步长为10
print([next(c), next(c), next(c)])
# [0, 10, 20]

# 累积计数器
a = [1, 3, 8, 20]
b = itl.accumulate(a)	# accumulate返回一个a的累积迭代器
print(list(b))
# [1, 4, 12, 33]

# 分组迭代器
v = [1, 2, 2, 3, 3, 6]
g = itl.groupby(v)
print([(k, list(t)) for k, t in g])

# 排列迭代器
print(list(itl.permutations('abc', 2)))

# 组合迭代器
print(list(itl.combinations("abc", 2)))
