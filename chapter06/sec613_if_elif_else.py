# coding: utf8

a, b, c = 5, 3, 7

# 找出a，b，c中的最大值
if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
elif b >= c:
    print(b)
else:
    print(c)
