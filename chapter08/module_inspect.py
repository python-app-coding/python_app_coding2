# coding: utf8
"""
观察程序在运行或导入时，__file__、__name__、sys.argv[0]、sys.path[0]
通过在不同路径运行、导入模块文件，查看这些属性的变化
调用方式：
    1. 在本目录以主程序运行
    2. 在其他目录以主程序运行
    3. 在本目录以模块方式运行
    4. 在其它目录以模块方式运行
    5. 在本目录导入
    6. 在其他目录导入
"""
import os.path
import sys


if __name__ == '__main__':
    status = "运行"
else:
    status = "导入"

print(f"*** 当模块{status}时，sys.argv[0], sys.path[0]及有关模块属性的取值情况 ***")
print(f'sys.argv[0]:\t{sys.argv[0]}')
print(f'sys.path[0]:\t{sys.path[0]}')
print(f'__file__:\t{__file__}')
# print(f'__name__:\t{__name__}')
# print(f'__package__:\t{__package__}')
if __spec__:
    # print(f'__spec__.parent:\t{__spec__.parent}')
    print(f'__spec__.origin:\t{__spec__.origin}')
# print(f"abspath(__file__):{os.path.abspath(__file__)}")
