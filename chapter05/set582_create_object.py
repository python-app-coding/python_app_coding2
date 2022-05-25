# coding: utf8


class Foo:
    p = 100

    def __init__(self, x=1):
        self.x = x
        print("object.x = {}".format(self.x))

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        print("Object is created!")
        return obj

    def m1(self, y):
        print(self.x, y)

    @classmethod
    def m2(cls, y):
        print(cls.p, y)

    @staticmethod
    def m3(z):
        print(Foo.p, z)


class Student:
    """学生信息管理类"""               # 说明类功能

    school = "洛河一中"               # 定义类变量
    address = "学生大街1号"

    # 初始化方法
    def __init__(self, name=""):
        self.name = name            # 创建对象变量

    # 对象方法，使用self引用初始化后的对象
    def get_name(self):
        return self.name            # 返回对象变量name

    # 类方法， 使用类名直接调用，缺省参数为cls
    @classmethod
    def get_school(cls):
        return cls.school           # 返回类变量（类方法不能调用对象变量！）

    # 静态方法, 使用类名直接调用，无缺省参数
    @staticmethod
    def get_addr():
        return Student.address      # 需要通过类名引用类变量



if __name__ == "__main__":
    # demo Foo
    foo = Foo(10)
    foo.m1(20)
    Foo.m2(20)
    Foo().m2(30)
    Foo.m3(40)
    Foo().m3(50)

    # demo Student
    print("Student attributes and methods:")
    print(Student.school)
    print(Student.get_addr())
    print(Student.get_school())

    print("Student('Li Fang')")
    st = Student("Li Fang")
    print("st.get_name():", st.get_name())
    print("st.name:", st.name)
    print("st.school:", st.school)
    print("st.get_school:", st.get_school())

    # change class attribute
    st2 = Student()
    print("st2.get_school():", st2.get_school())
    Student.school = "黄海二中"
    print("Student.school = 黄海二中")
    print("st2.get_school():", st2.get_school())

    # change object attributes
    st3 = Student()
    st3.name = "name3"
    st4 = Student()
    st4.name = "name4"
    print(st3.name, st4.name)
