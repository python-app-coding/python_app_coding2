# coding = utf8

"""
# 99乘法表的文本行列表lines可以存放在二进制文件中：

>>> import pickle

>>> lines = []
>>> for i in range(1,10):
...     line = ''
...     for j in range(1, i+1):
...         line += '{} x {} = {:2d}  '.format(i, j, i*j)
...     lines.append(line+'\\n')

>>> for line in lines:
...     print(line, end='')     # doctest: +NORMALIZE_WHITESPACE
1 x 1 =  1
2 x 1 =  2  2 x 2 =  4
3 x 1 =  3  3 x 2 =  6  3 x 3 =  9
4 x 1 =  4  4 x 2 =  8  4 x 3 = 12  4 x 4 = 16
5 x 1 =  5  5 x 2 = 10  5 x 3 = 15  5 x 4 = 20  5 x 5 = 25
6 x 1 =  6  6 x 2 = 12  6 x 3 = 18  6 x 4 = 24  6 x 5 = 30  6 x 6 = 36
7 x 1 =  7  7 x 2 = 14  7 x 3 = 21  7 x 4 = 28  7 x 5 = 35  7 x 6 = 42  7 x 7 = 49
8 x 1 =  8  8 x 2 = 16  8 x 3 = 24  8 x 4 = 32  8 x 5 = 40  8 x 6 = 48  8 x 7 = 56  8 x 8 = 64
9 x 1 =  9  9 x 2 = 18  9 x 3 = 27  9 x 4 = 36  9 x 5 = 45  9 x 6 = 54  9 x 7 = 63  9 x 8 = 72  9 x 9 = 81

>>> with open('temp_table99.pkl', 'wb') as f:
...     pickle.dump(lines, f)

# 再次使用时不需要计算，直接从文件中读出lines_str：
>>> with open('temp_table99.pkl', 'rb') as f:
...     read_lines = pickle.load(f)

>>> for line in read_lines:
...     print(line, end='')     # doctest: +NORMALIZE_WHITESPACE
1 x 1 =  1
2 x 1 =  2  2 x 2 =  4
3 x 1 =  3  3 x 2 =  6  3 x 3 =  9
4 x 1 =  4  4 x 2 =  8  4 x 3 = 12  4 x 4 = 16
5 x 1 =  5  5 x 2 = 10  5 x 3 = 15  5 x 4 = 20  5 x 5 = 25
6 x 1 =  6  6 x 2 = 12  6 x 3 = 18  6 x 4 = 24  6 x 5 = 30  6 x 6 = 36
7 x 1 =  7  7 x 2 = 14  7 x 3 = 21  7 x 4 = 28  7 x 5 = 35  7 x 6 = 42  7 x 7 = 49
8 x 1 =  8  8 x 2 = 16  8 x 3 = 24  8 x 4 = 32  8 x 5 = 40  8 x 6 = 48  8 x 7 = 56  8 x 8 = 64
9 x 1 =  9  9 x 2 = 18  9 x 3 = 27  9 x 4 = 36  9 x 5 = 45  9 x 6 = 54  9 x 7 = 63  9 x 8 = 72  9 x 9 = 81
"""