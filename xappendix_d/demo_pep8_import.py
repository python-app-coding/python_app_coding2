# coding = utf8

"""
使用导入语句import，要遵循的规范：
1）导入应放在模块的顶部，紧跟在模块注释之后，在全局变量和常数定义之前。
2）导入的顺序应该是：标准库、第三方库、本地应用库。
3）每个import只导入一个模块或包，或从一个库中导入相关模块或对象。
4）提倡使用绝对导入,尽量避免模糊导入：import *。
5）任何模块属性变量，如__version__、__all__、__author__等，要放在导入之前。
   但是，语句from __future__ import ...必须放在模块的所有代码之前，紧跟在模块注释之后。


This is the example module.
This module show some formats.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'
MAX_NUM = 10000

import os
import sys
