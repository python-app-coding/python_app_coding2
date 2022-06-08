# coding = utf8

for i in range(1,10):
    line_str = ''
    for j in range(1, i+1):
        line_str += '{} x {} = {}  '.format(i, j ,i*j)
    print(line_str)

# 生成文本写入文件
f = open('temp_product_99_table.txt', 'w', encoding='utf8')
for i in range(1,10):
    line_str = ''
    for j in range(1, i+1):
        line_str += '{} x {} = {:2d}  '.format(i, j, i*j)	    # 输出乘积项使用两位整数，保持对齐
    f.write(line_str+'\n')
f.close()

# 另一种生成文本方式
lines = []
for i in range(1,10):
    line = ''
    for j in range(1, i+1):
        line += '{} x {} = {:2d}  '.format(i, j, i*j)
    lines.append(line+'\n')
# 将文本写入文件
f = open('temp_product_99_table2.txt', 'w', encoding='utf8')
f.writelines(lines)
f.close()
