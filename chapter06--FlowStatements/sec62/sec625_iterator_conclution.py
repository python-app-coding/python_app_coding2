# coding = utf8

"""
>>> import itertools as itt

# product生成叉积
>>> print(list(itt.product('ab', repeat=2)))
[('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b')]

# permutations生成排列
>>> print([''.join(x) for x in list(itt.permutations('123'))])
['123', '132', '213', '231', '312', '321']

# combinations生成组合
>>> print([''.join(x) for x in list(itt.combinations('ABCD', 2))])
['AB', 'AC', 'AD', 'BC', 'BD', 'CD']

# 无限序列生成器，0，1，2，...
>>> xrange = itt.count()
>>> for x in xrange:
...    print(x, end=' ')
...    if x > 10:
...        break        # doctest: +REPORT_NDIFF +NORMALIZE_WHITESPACE
0 1 2 3 4 5 6 7 8 9 10 11

# 从一个序列得到累积值生成器
>>> acc = itt.accumulate([1, 2, 3, 4, 5])
>>> print(list(acc))
[1, 3, 6, 10, 15]

# 对字符串进行分组计算（对排序后的序列更有效）
>>> group = itt.groupby('aaacccdddaabbb')
>>> for k, g in group:
...     print(k, '：', list(g))
a ： ['a', 'a', 'a']
c ： ['c', 'c', 'c']
d ： ['d', 'd', 'd']
a ： ['a', 'a']
b ： ['b', 'b', 'b']

# 无穷等距增长数列迭代器
>>> c = itt.count(0, 10)		# 从0开始，步长为10
>>> print([next(c), next(c), next(c)])
[0, 10, 20]

# can't stop!!!
# print([x for x in itertools.count(30) if x < 35])
"""
