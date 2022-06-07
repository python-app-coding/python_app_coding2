# coding: utf8


class Foo:
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        print("Object is created!")
        return obj

    def __init__(self, x):
        self.x = x


foo = Foo(100)
print("foo.x = ", foo.x)


class Foo2:
    def __new__(cls, *args, **kwargs):  # 重新对象创建方法__new__
        print("object is created!")
        return None			            # 返回创建的对象

    def __init__(self, x):		        # 定义对象初始化方法
        print("Object is initialized!")  # 新增创建过程代码
        self.x = x			            # 设置对象属性


foo2 = Foo2(100)
print(type(foo2))


class Student:
    """学生信息管理类"""			# 说明类功能

    school = "洛河一中"			# 定义类变量
    address = "学生大街1号"

    def __init__(self, name="", age=18):		# 初始化方法
        self.name = name			# 创建对象变量

    def get_name(self):			# 对象方法，使用self引用初始化后的对象
        return self.name			# 返回对象变量name

    @classmethod				# 类方法， 使用类名直接调用，缺省参数为cls
    def get_school(cls):
        return cls.school			# 返回类变量（类方法不能调用对象变量！）

    @staticmethod				# 静态方法, 使用类名直接调用，无缺省参数
    def get_addr():
        return Student.address			# 需要通过类名引用类变量


print(Student.school)		    # 类属性可以使用类名直接引用
print(Student.get_addr())		# 静态方法可以使用类名直接调用
print(Student.get_school())		# 类方法可以使用类名直接调用

st1 = Student("Li Fang")		# 类初始化创建对象
st1.get_name()		            # 使用对象方法得到对象属性
# "Li Fang"
print(st1.name)			        # 对象引用对象属性
# "Li Fang"
print(st1.school)			    # 对象可以引用类属性（类属性为类的对象共享）
"洛河一中"
print(st1.get_school())
# "洛河一中"


Student.school = '黄海二中'	# 改变类属性
print(st1.get_school())		# 已经创建的对象的类属性随之改变
# '黄海二中'
st2 = Student()
print(st2.get_school())		# 使用了新的类属性
# '黄海二中'

st1.name = 'name01'		# 改变对象st1的属性name
st2.name = 'name02'		# 改变对象st2的属性name
print(st1.name, st2.name)		# 两个对象的属性name各自具有自己的值
# 'name01', 'name02'

