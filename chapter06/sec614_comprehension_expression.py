# coding = utf8


print([n for n in [1, 2, 3, 4, 5] if n < 5])	    # 从已有列表生成列表

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print([[m*n for n in a[:m]] for m in a])

print([m*n for n in a if n<3 for m in a[:n] if m*n < 10])

print({k: v for k, v in zip('abc', '123')})

print({k: v for k, v in zip('abc', '123') if k != 'b'})

print({k: None for k in 'abc'})

from unicodedata import name
print({chr(ci) for ci in range(0, 256) if 'DIGIT' in name(chr(ci), '')})
