# coding: utf8		# 代码文件编码

x = 100		        # 模块变量


def fun(a, b=2):		                    # 模块函数
    return a**b


class Class:		                        # 模块类
    def __init__(self):
        print('my class initialized!')	    # 类实例化为对象时，初始化时运行的代码


# 显示模块的两个重要属性: __name__, __file__
print('__name__ = {}'.format(__name__))
print('__file__ = {}'.format(__file__))


# 当模块作为执行程序时，__name__的值为'__main__'
if __name__ == '__main__':
    print('module executed!')	            # 模块执行时，打印信息
