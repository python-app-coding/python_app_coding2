# coding = utf8

"""
测试被装饰的类：
# 生成新的类new_class
>>> new_class = UserClass()

# 查看类变量是否发生了改变
>>> print('new_class.x = {}, new_class.y = {}'.format(new_class.x, new_class.y))
new_class.x = 1000, new_class.y = 2000

# 使用增加的方法
>>> print('new_class.add_method() = {}'.format(new_class.add_method()))
new_class.add_method() = 3000

# 创建对象obj
>>> obj = new_class(5000)
>>> print(obj.z)		        # 调用对象属性
5000

>>> print(obj.add_method())	    # 调用增加的类方法
3000
"""


class ClassDecClass:
    def __init__(self, cls):
        self._cls = cls

    def __call__(self):
        # 修改被装饰的类，改变类属性x，增加类属性y，增加类方法add_method
        self._cls.x = 1000
        self._cls.y = 2000

        # 为被装饰的类增加新的方法
        @classmethod
        def add_method(cls):
            return cls.x + cls.y

        self._cls.add_method = add_method
        return self._cls


# 使用类装饰器装饰类：
@ClassDecClass
class UserClass:
    x = 100		        # 类变量

    def __init__(self, z=None):
        self.z = z		# 对象变量
