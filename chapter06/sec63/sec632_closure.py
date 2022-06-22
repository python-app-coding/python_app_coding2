# coding = utf8


def get_closure():	            # 产生闭包函数的封装函数
    x = 1		            # 自由变量
    print(hex(id(x)))

    def closure():          # 闭包函数
        nonlocal x	        # 声明x为非局部变量
        x = x + 1
        print(hex(id(x)))   # 引用过程中，变量指向的对象发生了改变
        return x

    return closure	        # 返回闭包函数


# 获取闭包函数
cf = get_closure()
# 调用闭包函数
print(sum(cf() for _ in range(10)))
#
print(cf.__closure__)
