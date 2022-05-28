# coding: utf8


class Father:
    p = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_values(self):
        return self.p, self.x, self.y


class Son(Father):

    def __init__(self, x, y, z):
        # super().__init__(x, y)
        Father.__init__(self, x, y)
        self.z = z

    def get_values(self):
        return *super().get_values(), self.z

    def get_values2(self):
        return *Father.get_values(self), self.z


if __name__ == "__main__":
    print("Father(1, 2).get_values(): ", Father(1, 2).get_values())
    print("Son(1, 2, 3).get_values(): ", Son(1, 2, 3).get_values())
    print("Son(1, 2, 3).get_values2(): ", Son(1, 2, 3).get_values2())
