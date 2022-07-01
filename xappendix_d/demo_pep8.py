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


if __name__ == '__main__':
    demo_indent()

