# coding = utf8

from glob import glob
import os

tdir = os.path.abspath('.')

# 使用*搜索当前目录的子目录及文件
print("使用*搜索当前目录的子目录及文件:")
print("glob('~/*')")
print('\n'.join(glob(tdir+'/../*')))
print("")

# 使用*.*仅搜索文件
print("使用*.*仅搜索文件:")
print("glob('~/*.*')")
print('\n'.join(glob(tdir+'/*.*')))
print("")

# 使用.*仅搜索有后缀名称文件
print("使用.*仅搜索有后缀名称文件")
print("glob('~/.*')")
print('\n'.join(glob(tdir+'/../.*')))
print("")

# 使用**仅搜索有名称的文件或目录
print("使用**仅搜索有名称的文件或目录:")
print("glob('~/**')")
print('\n'.join(glob(tdir+'/../**')))
print("")

# 递归搜索
print("递归搜索:")
print("glob('~/**'， recursive=True)")
print('\n'.join(glob(tdir+'/**', recursive=True)))
print("")

# 不使用通配符时为严格匹配，只搜索指定名称目录或文件
print("不使用通配符时为严格匹配，只搜索指定名称目录或文件:\n"
      "glob('~/')")
print('\n'.join(glob(tdir)))
print("")
