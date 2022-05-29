# coding: utf8


for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}*{j} = {i*j}")  # 打印9-9乘法表，f表达式需要Python3.6以上版本支持

for i in range(1, 10):
    line = ""
    for j in range(1, 10):
        if j > i:
            break
        line += f"{j}*{i}={i*j} "
    print(line)
else:
    print('—-- end ---')
