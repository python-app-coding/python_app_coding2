# coding: utf8
"""
观察程序在运行或导入时，各有关属性的取值__file__、__name__、sys.argv[0]、sys.path[0]
when import or run, inspect attributes: __file__、__name__、sys.argv[0]、sys.path[0]
以下面方式运行本模块：
run or import this module:
1. 在本目录以主程序运行 python module, at own directory
2. 在其他目录以主程序运行 python module, at other directory
3. 在本目录以模块方式运行 run -m module, at own directory
4. 在其它目录以模块方式运行 python -m module, at other directory
5. 在本目录导入 import module at own directory
6. 在其他目录导入 import module at other directory
"""

import sys


if __name__ == '__main__':
    status = "run"
else:
    status = "import"

print(f"Module status: {status}")
print('-'*80)
print(f'sys.argv[0]:\t{sys.argv[0]}')
print(f'sys.path[0]:\t{sys.path[0]}')
print(f'__file__:\t{__file__}')
print(f'__name__:\t{__name__}')
print(f'__package__:\t{__package__}')
if __spec__:
    print(f'__spec__.parent:\t{__spec__.parent}')
    print(f'__spec__.origin:\t{__spec__.origin}')
# print(f"abspath(__file__):{os.path.abspath(__file__)}")
print('-'*80)
