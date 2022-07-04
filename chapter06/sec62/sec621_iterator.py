# coding: utf8


import itertools as itl

# 无穷计数器
c = itl.count(0, 10)	    # 从0开始，步长为10
print([next(c), next(c), next(c)])
# [0, 10, 20]

# 累积计数器
a = [1, 3, 8, 20]
b = itl.accumulate(a)	    # accumulate返回一个a的累积迭代器
print(list(b))
# [1, 4, 12, 33]

# 分组迭代器
# 在使用groupby之前，最后将来源序列排序
# 返回一个字典，以非重复元素为键，出现的各个元素组成列表为值
v = [1, 2, 2, 3, 3, 6]
g = itl.groupby(v)
print([(k, list(t)) for k, t in g])
# [(1, [1]), (2, [2, 2]), (3, [3, 3]), (6, [6])]

# 排列迭代器
# 从一个序列中提取排列，每次返回一个元组
perm = itl.permutations('abc', 2)
print(list(perm))
# [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]

# 组合迭代器
# 从一个序列中提取组合，每次返回一个元组
comb = itl.combinations("abc", 2)
print(list(comb))
# [('a', 'b'), ('a', 'c'), ('b', 'c')]
