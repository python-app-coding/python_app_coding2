# coding=utf8

import math
import random

# 求平方根
print("square root of 2 is ", math.sqrt(2))

# 求1-100的和
s = sum(range(1, 101))
print(f"The sum of 1-100 is {s}")

# 求1-12345之间平方数的个数
c = [k for k in range(12345) if math.sqrt(k) == int(math.sqrt(k))]
print(f"The count of square number of 0-12345 is {len(c)}, {c[0:5]} ...")

# 求接近的数
nums = [random.randint(1, 100) for _ in range(20)]
print(nums)
result = []
for n1 in range(len(nums)):
    for n2 in range(n1+1, len(nums)):
        if abs(nums[n1]-nums[n2]) < 5:
            result.append((n1, n2))
            print((n1, nums[n1]), (n2, nums[n2]))
