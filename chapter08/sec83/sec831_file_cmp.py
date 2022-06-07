# coding = utf8
import difflib


with open("cmpfile01.txt", 'wt') as fp01, open("cmpfile02.txt", 'wt') as fp02:
     fp01.writelines(
         "this is line01\n"
         "this is line02\n"
         "this is line03\n")
     fp02.writelines(
         "this is line0102\n"
         "this is line02\n"
         "this is line0203\n"
         "this is line0204\n")

with open('cmpfile01.txt') as fp1, open('cmpfile02.txt') as fp2:
    lines1 = fp1.readlines()
    lines2 = fp2.readlines()
    for line in difflib.Differ().compare(lines1, lines2):
        print(line, end='')
# 比较结果(-: 第一文件的文本， +: 第二文件的文本， ？: 标识差异位置， ' ':两个文本行相同的内容)
# - this is line01
# + this is line0102
# ?               ++	# 在该位置出现不同
#   this is line02	# 该行都相同
# - this is line03
# + this is line0203
# ?              ++	# 在该位置出现不同
# + this is line0204	# 该行只在第二个文件存在


s = difflib.SequenceMatcher(a="abxcd", b="abcd")	# 比较两个字符串（字符序列）
cr = s.get_matching_blocks()	    # 比较结果是元素为命名元组的列表
for m in cr:
    print(m)
# Match(a=0, b=0, size=2),			# 0位置开始2个字符相同,即a[0:2] == b[0:2]
# Match(a=3, b=2, size=2), 			# a=3,b=2位置，2个字符相同,a[3:5] == b[2:4]
# Match(a=5, b=4, size=0)			# 最后一个是无效结果（dummy）