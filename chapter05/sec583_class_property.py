# coding: utf8


class Person:
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 200:
            self.__age = age    # 实际存储在私有属性中
        else:
            raise ValueError("age must be in [0, 199]")


class Person2:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 200:
            self.__age = age    # 实际存储在私有属性中
        else:
            raise ValueError("age must be in [0, 199]")


class Person3:
    age = 99
    @property
    def age(self):
        return 100


class Person4:
    def __init__(self):
        # self.age = 99     # AttributeError: can't set attribute
        pass

    @property
    def age(self):
        return 100


if __name__ == '__main__':
    p1 = Person()
    print([p for p in dir(p1) if p.startswith('_') and not p.endswith('__')])
    p1.age = 20
    print([p for p in dir(p1) if p.startswith('_') and not p.endswith('__')])
    # p1.age = 210    # ValueError: age must be in [0, 199]
    # p1.age = -2     # ValueError: age must be in [0, 199]

    p2 = Person2(30)
    print(p2.age)
    # print([p for p in dir(p1) if p.startswith('_') and not p.endswith('__')])
    # p2.age = 300      # # ValueError: age must be in [0, 199]

    # 类属性值不会赋值给特性，类属性被特性所遮盖
    print("Person3.age = ", Person3.age)
    # 实例化后，类属性的值age=100仍然被特性age遮盖
    p3 = Person3()
    print("Person3().age = ", p3.age)
    # 没有实现setter方法时，不允许对特性赋值
    # p3.age = 102
    print("vars(p3): ", vars(p3))
    # 类属性仍然被特性覆盖
    print("Person3.age = ", Person3.age)

    p4 = Person4()
    print("Person4().age = ", p4.age)
    # 创建一个实例变量age，但调用时仍然使用特性取值方法，返回类属性值
    p4.__dict__['age'] = 105
    print("Person4().age = ", p4.age)
