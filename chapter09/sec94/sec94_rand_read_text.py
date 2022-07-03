# coding = utf8

import linecache as lc
import os

with open("temp_linecache.txt", 'w') as fp:
    for i in range(100):
        fp.write(f'line-{i}\n')

with open("temp_linecache_fixed_length.txt", 'w') as fp:
    for i in range(100):
        fp.write(f'line-{i:03d}\n')

# 定长文本行的随机访问：
def rand_read_text(file, lineno):
    with open(file, 'r') as fp:
        line = fp.readline()
        rowlen = len(line) + len(os.linesep) - 1  # 在Windows中，会减少一个\r
        fp.seek((lineno-1)*rowlen, 0)
        return fp.readline()                      # 定位到要读取的行


# 变长文本行的随机读写：
def rand_read_text2(file, lineno):
    with open(file) as fp:
        for j in range(lineno):                  # 逐行读取，返回最后的行
            line = fp.readline()
        return line


if __name__ == '__main__':
    # 读取定长文本行
    print(rand_read_text('temp_linecache_fixed_length.txt', 50))
    print(rand_read_text('temp_linecache_fixed_length.txt', 100))

    # 读取变长文本行
    print(rand_read_text2('temp_linecache.txt', 50))

    # 使用linecache随机读取文本行：
    line = lc.getline('temp_linecache.txt', 50)
    print("line 50 in temp_linecache.txt: ", line)
    line = lc.getline('temp_linecache.txt', 150)
    print("no line 150 in temp_linecache.txt: ", line)
    line = lc.getline('temp_linecache_nofile.txt', 50)
    print("no file return empty string: ", line)
