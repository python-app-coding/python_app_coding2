# coding = utf8

# 99乘法表的文本行列表lines可以存放在二进制文件中：
import pickle

lines = []
for i in range(1,10):
    line = ''
    for j in range(1, i+1):
        line += '{} x {} = {:2d}  '.format(i, j, i*j)
    lines.append(line+'\n')
print(lines)
with open('temp_table99.pkl', 'wb') as f:
    pickle.dump(lines, f)

# 再次使用时不需要计算，直接从文件中读出lines_str：
with open('table99.pkl', 'rb') as f:
    read_lines = pickle.load(f)
    print(read_lines)
