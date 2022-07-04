# coding: utf8


# 使用双循环打印9-9乘法表，f表达式需要Python3.6以上版本支持
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}*{j} = {i*j}")

# 使用双循环，按照阶梯格式打印9-9乘法表
for i in range(1, 10):
    line = ""
    for j in range(1, 10):
        if j > i:
            break
        line += f"{j}*{i}={i*j} "
    print(line)
else:
    print('—-- end ---')
