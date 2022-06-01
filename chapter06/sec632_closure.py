# coding = utf8


def create_closure(p1=1):	    # 产生闭包函数的封装函数
    x1 = 1		                # 自由变量
    x2 = 2

    def closure(p2=2):          # 闭包函数
        nonlocal x2	        # 声明x为非局部变量
        x2 = x1 + p1 + p2
        print(id(x1), id(x2), id(p1), id(p2))
        return x2

    return closure	    # 返回闭包函数


cf = create_closure()
print(cf())
print(cf.__closure__)
