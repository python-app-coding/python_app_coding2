# coding: utf8

"""
集合创建示例：
>>> s = {1, 2}		# 使用字面定义方式建立集合
>>> d = {'year': 1979, 'month': 7, 'day': 7}

>>> set(d.keys())	#从字典d的键的值生成一个集合, 输出的顺序是不确定的！
{'year', 'month', 'day'}

>>> set([1, 2, 1, 3, 2])	# 从列表得到一个集合,重复的元素会筛出，只保留一个
{1, 2, 3}


集合运算示例：
>>> s1 = {1, 2, 3}
>>> s2 = {1, 2, 4}

# 求交集
>>> s1 & s2
{1, 2}

# 求并集
>>> s1 | s2
{1, 2, 3, 4}

# 求差集：{x: x属于被减集合，x不属于所减集合}
>>> s1 - s2, s2 - s1
({3}, {4})

# 求对称差集: {x: x 仅属于s1和s2中的一个}
>>> s1 ^ s2
{3, 4}

# 包含比较（包含运算优先级小于交、并、差运算）
>>> s1 > s2, s1-{3} >= s2-{4}
(False, True)

# 元素包含运算
>>> 3 in s1, 3 in s2
(True, False)


【集合方法】

1.增加元素方法
◎ set.add(e)
向集合中添加一个元素。如果集合中已经存在该元素，不作任何处理。
>>> set1 = {1, 2, 3}
>>> set1.add(5)
>>> set1
{1, 2, 3, 5}
>>> set1.add(1)
>>> set1
{1, 2, 3, 5}

◎ set.update(set2)
使用集合set2中的元素更新集合set。相当于两个集合的并。更新后集合set被改变。
>>> set1 = {1, 2, 3}
>>> set2 = {4, 5, 6}
>>> set1.update(set2)
>>> set1
{1, 2, 3, 4, 5, 6}


2.删除元素方法
◎ set.clear
清除集合中的所有元素。应谨慎使用。
>>> set1 = {1, 2, 3}
>>> set1.clear()
>>> set1
set()

◎ set.discard(e)
从集合中去除元素e。如果e不在集合中，则不做任何处理。
>>> set1 = {1, 2, 3}
>>> set1.discard(1)
>>> set1
{2, 3}

◎ set.remove(e)
从集合中去除元素e。如果e不在集合中，触发异常KeyError。
>>> set1 = {1, 2, 3}
>>> set1.remove(1)
>>> set1
{2, 3}

# >>> set1.remove(9)
# ...
# KeyError: 9

◎ set.pop()
从集合中弹出任何一个元素，如果集合为空时，触发异常KeyError。
>>> set1 = {1, 2}
>>> set1.pop()
1
>>> set1.pop()
2

# >>> set1.pop()
# ...
# KeyError: 'pop from an empty set'

3.判断方法
◎ set.isdisjoint(set2)
判断两个集合是否无交集。如果交集为空，返回True，否则返回False。
>>> set1 = {1, 2, 3}
>>> set2 = {1, 3, 5}
>>> set3 = {7, 8, 9}
>>> set1.isdisjoint(set2)
False
>>> set1.isdisjoint(set3)
True

◎ set.issubset(set2)
判断集合set是包含于set2，即是否为set2的子集。如为子集，返回True，否则返回False。
◎ set.insuperset(set2)
判断集合set是包含set2，即set2是否为set的子集。如包含set2，返回True，否则返回False。
>>> set1 = {1, 2, 3}
>>> set2 = {1, 3, 5}
>>> set3 = {1, 2}
>>> set1.issubset(set2)		# set1不是set2的子集
False
>>> set3.issubset(set1)		# set3为set1的子集
True
>>> set1.issuperset(set3)		# set1包含set3
True


4.运算方法
◎ set.difference(set2)
返回集合set和set2 的差集。
>>> set1 = {1,2,3}
>>> set2 = {3,4}
>>> set1.difference(set2)
{1, 2}

◎ set.difference_update(set2)
返回集合set和set2 的差集，并将集合更新为差集。
>>> set1 = {1, 2, 3}
>>> set2 = {3, 4}
>>> set1.difference_update(set2)
>>> set1
{1, 2}

◎ set.intersection(set2)
返回集合set和set2 的交集。
>>> set1 = {1,2,3}
>>> set2 = {3,4}
>>> set1.intersection(set2)
{3}

◎ set.intersection_update(set2)
返回set于set2的交集，并将set更新为交集。
>>> set1 = {1,2,3}
>>> set2 = {3,4}
>>> set1.intersection_update(set2)
>>> set1
{3}

◎ set.symmetric_difference(set2)
返回set与set2的对称差集，二者的并集去除交集的元素。
>>> set1 = {1,2,3}
>>> set2 = {3,4}
>>> set1.symmetric_difference(set2)
{1, 2, 4}

◎ set.symmetric_difference_update()
返回set与set2的对称差集，并将set赋值为对称差集。
>>> set1 = {1, 2, 3}
>>> set2 = {3, 4}
>>> set1.symmetric_difference_update(set2)
>>> set1
{1, 2, 4}

◎ set.union(set2)
返回集合set与集合set2的并集。
>>> set1 = {1,2,3}
>>> set2 = {3,4}
>>> set1.union(set2)
{1, 2, 3, 4}
"""