# coding = utf8

from unicodedata import name

# 从已有列表生成列表
print([n for n in [1, 2, 3, 4, 5] if n < 5])

# 嵌套循环
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print([[m*n for n in a[:m]] for m in a])

# 在多循环中使用条件判断筛选
print([m*n for n in a if n<3 for m in a[:n] if m*n < 10])

# 由zip生成二元元组为元素的迭代器，用于字典推导式
print({k: v for k, v in zip('abc', '123')})

# 在字典推导式中使用条件判断筛选
print({k: v for k, v in zip('abc', '123') if k != 'b'})

# 由序列生成缺省值为None的字典
print({k: None for k in 'abc'})

# 通过字符名称筛选字符0..9
print({chr(cn) for cn in range(0, 256) if 'DIGIT' in name(chr(cn), '')})
