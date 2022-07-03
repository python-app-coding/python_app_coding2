# coding: utf8

"""
模块可以通过导入、主程序等方式运行，
不同运行方式下，其有关属性的值是不同的。
"""

import os
import os.path as osp
import sys


def argv(byimport=True):
    """
    测试模块以不同方式运行时一些状态的变化
    运行参数: sys.argv，
    加载检索路径: sys.path，
    特殊属性: __file__, __name__
    当前工作路径os.getcwd(), os.path.abspath('.'), sys.path[-1]
    """
    # sys: sys.argv when running as python program
    print('sys attrs:')
    print('    sys.argv = {}'.format(sys.argv))
    if not byimport:
        if len(sys.argv) > 2:
            print('    argv[1] * argv[2]={}'.
                  format(int(sys.argv[1])*int(sys.argv[2])))
    print("    sys.path= ['{}', {}, '{}']\n".format(sys.path[0], '...', sys.path[-1]))

    # module attr: __file__ and __name__
    print('module attrs:')
    print('   module.__file__  = {}'.format(__file__))
    print('   module.__name__  = {}\n'.format(__name__))

    # os: current work path
    print('current path:')
    print('          os.getcwd() = {}'.format(os.getcwd()))
    print(' os.path.abspath(".") = {}'.format(osp.abspath("../../chapter03")))
    print('         sys.path[-1] = {}\n'.format(sys.path[-1]))


# module.__name__
if __name__ == '__main__':
    print('module run as program...')
    argv(False)
else:
    print('module loaded through importing ...')
    argv(True)
