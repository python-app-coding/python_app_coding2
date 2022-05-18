# coding: utf8
"""
观察程序在运行或导入时，各有关属性的取值__file__、__name__、sys.argv[0]、sys.path[0]
when import or run, inspect attributes: __file__、__name__、sys.argv[0]、sys.path[0]

以下面方式运行本模块 run or import this module following modes below：
module location: D:\python_app_coding\chapter08\module_attrs.py

1. 在本目录以主程序运行
    [own directory]> python module

    (venv) D:\python_app_coding\chapter08>python module_attrs.py
    Module status: run
    --------------------------------------------------------------------------------
    __file__:       D:\python_app_coding\chapter08\module_attrs.py
    __name__:       __main__
    sys.argv[0]:    module_attrs.py
    sys.path[0]:    D:\python_app_coding\chapter08
    --------------------------------------------------------------------------------

2. 在其他目录以主程序运行
    [other directory]> python module

    (venv) D:\python_app_coding>python chapter08\module_attrs.py
    Module status: run
    --------------------------------------------------------------------------------
    __file__:       D:\python_app_coding\chapter08\module_attrs.py
    __name__:       __main__
    sys.argv[0]:    chapter08\module_attrs.py
    sys.path[0]:    D:\python_app_coding\chapter08
    --------------------------------------------------------------------------------

3. 在本目录以模块方式运行
    [own directory]> python -m module

    (venv) D:\python_app_coding\chapter08>python -m module_attrs
    Module status: run
    --------------------------------------------------------------------------------
    __file__:       D:\python_app_coding\chapter08\module_attrs.py
    __name__:       __main__
    sys.argv[0]:    D:\python_app_coding\chapter08\module_attrs.py
    sys.path[0]:    D:\python_app_coding\chapter08
    __spec__.name:  module_attrs
    __spec__.parent:
    __spec__.origin:        D:\python_app_coding\chapter08\module_attrs.py
    --------------------------------------------------------------------------------

4. 在其它目录以模块方式运行
    [other directory]> python -m module

    (venv) D:\python_app_coding>python -m chapter08.module_attrs
    Module status: run
    --------------------------------------------------------------------------------
    __file__:       D:\python_app_coding\chapter08\module_attrs.py
    __name__:       __main__
    sys.argv[0]:    D:\python_app_coding\chapter08\module_attrs.py
    sys.path[0]:    D:\python_app_coding
    __spec__.name:  chapter08.module_attrs
    __spec__.parent:        chapter08
    __spec__.origin:        D:\python_app_coding\chapter08\module_attrs.py
    --------------------------------------------------------------------------------

5. 在本目录导入
    [own directory]> python
    > > > import module

    Module status: import
    --------------------------------------------------------------------------------
    __file__:           D:\python_app_coding\chapter08\module_attrs.py
    __name__:           module_attrs
    sys.argv[0]:
    sys.path[0]:
    __spec__.name:      module_attrs
    __spec__.parent:
    __spec__.origin:    D:\python_app_coding\chapter08\module_attrs.py
    --------------------------------------------------------------------------------

6. 在其他目录导入 import zt orhter directory
    [other directory]> python
    > > > import module_attrs

    Module status: import
    --------------------------------------------------------------------------------
    __file__:       D:\python_app_coding\chapter08\module_attrs.py
    __name__:       chapter08.module_attrs
    sys.argv[0]:
    sys.path[0]:
    __spec__.name:  chapter08.module_attrs
    __spec__.parent:        chapter08
    __spec__.origin:        D:\python_app_coding\chapter08\module_attrs.py
    --------------------------------------------------------------------------------

7. 在Ipython中导入
    []: import module
    Module status: import
    --------------------------------------------------------------------------------
    __file__:	D:\python_app_coding\chapter08\module_attrs.py
    __name__:	chapter08.module_attrs
    sys.argv[0]:	C:\Program Files\JetBrains\PyCharm 2021.1.2\plugins\python\helpers\pydev\pydevconsole.py
    sys.path[0]:	C:\Program Files\JetBrains\PyCharm 2021.1.2\plugins\python\helpers\pydev
    __spec__.name:	chapter08.module_attrs
    __spec__.parent:	chapter08
    __spec__.origin:	D:\python_app_coding\chapter08\module_attrs.py
    --------------------------------------------------------------------------------

"""

import sys


if __name__ == '__main__':
    status = "run"
else:
    status = "import"

print(f"Module status: {status}")
print('-'*80)
print(f'__file__:\t{__file__}')
print(f'__name__:\t{__name__}')
print(f'sys.argv[0]:\t{sys.argv[0]}')
print(f'sys.path[0]:\t{sys.path[0]}')

# 使用.py脚本作为主程序方式运行时，没有__spec__和__pakcage__属性
if __spec__:
    # print(f'__package__:\t{__package__}')     # same as __spec__.parent
    # print(f'__spec__:\t{__spec__}')           # __spec__ is importlib.machinery.ModuleSpec
    print(f'__spec__.name:\t{__spec__.name}')
    print(f'__spec__.parent:\t{__spec__.parent}')
    print(f'__spec__.origin:\t{__spec__.origin}')
print('-'*80)
