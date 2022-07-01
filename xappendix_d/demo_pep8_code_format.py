# coding: utf8
"""
pep8 demo 示例
"""


def demo_indent():
    for a in range(10):
        print(a)

    def long_function_name(
            var_one, var_two, var_three,
            var_four):
        print(var_one)
        return "success"

    var_one, var_two, var_three, var_four = 1, 2, 3, 4
    foo = long_function_name(var_one, var_two,
                             var_three, var_four)


def demo_line_feed():
    x = ('long long long long long long long long long long long long long long long'
         'long long long long long long long long long long long long long long long long string')
    print(x)


def demo_expression_line_feed(gross_wages, taxable_interest, student_loan_interest):
    income = (gross_wages
              + taxable_interest
              - student_loan_interest)
    return income


def demo_blank_line():
    # something to do
    a = sum(range(100))

    # do something2
    print(a)


def demo_blank_operand():
    # 逗号分隔符之后保留一个空格
    x, y, a, b = 1, 2, 3, 4

    # 运算符前后需要空格
    a = 3 + 4

    # 如果运算式中出现不同运算符的优先级组合，可以考虑取消高优先级运算符或括号内运算符前后的空格。
    hypot2 = x*x + y*y
    c = (a+b) * (a-b)

    # 不提倡使用行内注释！
    x = x*2 - 1		# minus 1 for something important

    # 括号（包括圆括号()、方括号[]、换括号{}）之内直接引用的对象，一般前后不留空格。
    ham = {1: 2}
    eggs = 3
    print(ham[1], {eggs: 2})

    # 冒号和分号之前不留空格，之后保留一个空格。
    # 括号内的冒号，视为运算符，前后不留空格。
    # 如果出现优先级或函数引用，冒号后边可以保留一个空格。
    ham = list(range(10))
    lower, upper, offset, step = 1, 5, 2, 1
    step_fn = lambda x: 10 if x < 5 else 5
    print(ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:])
    print(ham[lower:upper], ham[lower:upper:], ham[lower::step])
    print(ham[lower+offset:upper+offset])
    print(ham[: step_fn(1) : step_fn(6)], ham[:: step_fn(7)])


def demo_semicolon():
    # 不提倡的方式
    a = 1; b = 2


if __name__ == '__main__':
    # demo_indent()
    demo_blank_operand()
