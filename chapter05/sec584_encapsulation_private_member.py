# coding: utf8


class Foo:
    # 保护性类属性
    _p1 = 100
    # 私有性类属性
    __p2 = 200

    def __init__(self, x, y):
        # 开放对象属性
        self.x = x
        # 私有性对象属性
        self._y1 = y
        # 私有性对象属性
        self.__y2 = y+10

    # 保护性对象方法
    def _print_attrs(self):
        # 在对象方法中可以调用私有属性
        print("(__p2, x , __y2): ", self.__p2, self.x, self.__y2)

    def get_values(self):
        # 在对象方法中可以调用保护性方法
        self._print_attrs()
        return self.__p2, self.x, self._y1

    # 私有对象方法
    def __get_values(self):
        # 引用私有属性
        return self.__p2, self.x, self.__y2


class SubFoo(Foo):
    def show(self):
        self._print_attrs()	                    # 继承了的受保护方法
        # self.__get_values()	                # 引用父类私有方法

        print("SubFoo()._p1 = ", self._p1)	    # 引用继承的受保护对象属性
        print("SubFoo()._y1 = ", self._y1)	    # 引用继承的受保护对象属性

        # 直接引用私有属性触发异常
        try:
            print("self.__p2 = ", self.__p2)    # 未继承私有类属性
        except AttributeError as e:
            print("__p2 is inaccessible")
            # 引用更名后的私有属性
            print("SubFoo()._Foo__p2 = ", self._Foo__p2)


if __name__ == '__main__':
    # 直接引用保护类属性
    print("Foo._p1 = ", Foo._p1)	                # 引用受保护类属性

    print("SubFoo(1, 2).show():")
    SubFoo(1, 2).show()

    print("Foo() attributes:")
    print([p for p in dir(Foo(1, 2)) if p.startswith('_') and not p.endswith('__')])
    print("SubFoo() attributes:")
    print([p for p in dir(SubFoo(1, 2)) if p.startswith('_') and not p.endswith('__')])
