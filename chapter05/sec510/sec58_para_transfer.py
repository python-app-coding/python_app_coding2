# coding = utf8


a = 1000
b = [1, 2, 3]


def test_trans(x, y):
    print("id(x)=", id(x))
    print("id(y)=", id(y))
    print("y[0] = 1000")
    y[0] = 1000


print("id(a)=", id(a))
print("id(b)=", id(b))
test_trans(a, b)
print("b = ", b)


# 函数接收两个变量，交换两个参数对象的值：
def swap_value(x, y):
    x, y = y, x
    print('x=', x, 'y=', y)


# 函数的执行情况：
a, b = 100, 200	    # 外部变量
swap_value(a, b)    # 传递给函数
# x = 200 y = 100	# 在函数内部，两个变量的值发生了变化
print(a, b)	        # 外部变量并没有发生变化，说明传递参数的过程进行了复制，而不是引用
# 100, 200
