# coding: utf8


class MyClass:
    # define private attribute
    __p = 100

    def __init__(self, x, y):
        self.x = x
        # define object private member
        self.__y = y

    def __print_attrs(self):
        # 在对象方法中可以调用私有属性
        print(self.__p, self.x, self.__y)

    def get_values(self):
        # reference to private member
        self.__print_attrs()

    # private method
    def __get_values2(self):
        # reference to private member
        return self.__p, self.x, self.__y


if __name__ == "__main__":
    print("use __p by _MyClass__p: ", MyClass._MyClass__p)

    try:
        # ref __p will invoke Exception AttributeError
        print("use __p by MyClass.__p: ", MyClass.__p)
    except AttributeError as e:
        print(e)

    try:
        # ref private method will tigger Exception AttributeError
        print("call MyClass.__get_values2: ", MyClass.__get_values2())
    except AttributeError as e:
        print(e)


