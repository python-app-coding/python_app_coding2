# coding: utf8		                        # 声明文件编码

# 模块变量
x = 100


# 在模块中定义的函数
def fun(a, b=2):
    print("call fun")                       # 函数被调用时，执行其内部代码
    return a**b


# 在模块中定义的类
class Class:
    print("class in module")                # 导入或运行时，类定义代码执行
    def __init__(self):
        print('my class initialized!')	    # 类实例化为对象时，执行__init__方法代码


# 模块最常用的两个重要属性: __name__, __file__
print('__file__ = {}'.format(__file__))
if __name__ == '__main__':
    print('module is executed!')	        # 模块被执行
else:
    print(__name__)                         # 模块被导入

# 如果模块具有属性__path__, 则为一个包
try:
    print("__path__ = ", __path__)
except NameError as e:
    print(e)
finally:
    import pkm

# 其它模块属性
print("__spec__ = ", __spec__)              # 存放模块载入设置信息
print("__package__ = ", __package__)        # 模块所属于包的名称
print("__loader__ = ", __loader__)          # 模块装载器
print("__cached__ = ", __cached__)          # 模块编译文件存放路径
