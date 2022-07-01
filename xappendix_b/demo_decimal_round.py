# coding: utf8


import decimal as dc


def demo_decimal_setting():
    """
    decimal设置
    # decimal default setting
    >>> dc.getcontext()
    Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])

    # set precise
    >>> dc.getcontext().prec = 50

    # expression with decimal number
    >>> dc.Decimal(2) / dc.Decimal(3)
    Decimal('0.666..6667')
    """


def demo_round_ceiling():
    """
    ROUND_CEILING
    向正无穷大靠近。正数时进位，负数时舍去。

    >>> dc.getcontext().rounding = dc.ROUND_CEILING
    >>> round(dc.Decimal('1.14'), 1)
    Decimal('1.2')
    >>> round(dc.Decimal('-1.17'), 1)
    Decimal('-1.1')
    """


def demo_round_down():
    """
    ROUND_DOWN
    向0靠近。保留位之后一律舍去。

    >>> dc.getcontext().rounding = dc.ROUND_DOWN
    >>> round(dc.Decimal('1.16'), 1)
    Decimal('1.1')
    >>> round(dc.Decimal('-1.16'), 1)
    Decimal('-1.1')
    """


def demo_round_floor():
    """
    ROUND_FLOOR
    向负无穷靠近。大于0时舍去，小于0时进位。

    >>> dc.getcontext().rounding = dc.ROUND_FLOOR
    >>> round(dc.Decimal('1.16'), 1)
    Decimal('1.1')
    >>> round(dc.Decimal('-1.16'), 1)
    Decimal('-1.2')
    """


def demo_round_half_down():
    """
    ROUND_HALF_DOWN
    向最近数靠近，相同距离时靠近0。

    >>> dc.getcontext().rounding = dc.ROUND_HALF_DOWN
    >>> round(dc.Decimal('1.15'), 1)
    Decimal('1.1')

    >>> round(dc.Decimal('1.150001'), 1)
    Decimal('1.2')

    """


def demo_round_half_even():
    """
    ROUND_HALF_EVEN
    向最近数靠近，相同距离时靠近偶数。

    >>> dc.getcontext().rounding = dc.ROUND_HALF_EVEN
    >>> round(dc.Decimal('1.15'), 1)
    Decimal('1.2')
    >>> round(dc.Decimal('1.25'), 1)
    Decimal('1.2')
    """


def demo_round_half_up():
    """
    ROUND_HALF_UP
    向最近数靠近，相同距离时远离0。

    >>> dc.getcontext().rounding = dc.ROUND_HALF_UP
    >>> round(dc.Decimal('1.25'), 1)
    Decimal('1.3')
    >>> round(dc.Decimal('-1.25'), 1)
    Decimal('-1.3')
    """


def demo_round_up():
    """
    ROUND_UP
    向远离0方向靠近。正负数都选择进位。

    >>> dc.getcontext().rounding = dc.ROUND_UP
    >>> round(dc.Decimal('1.14'), 1)
    Decimal('1.2')
    >>> round(dc.Decimal('-1.14'), 1)
    Decimal('-1.2')
    """


def demo_round_05up():
    """
    ROUND_05UP
    如果最后位是0或5，采用远离0的方式进位，非0和5时以靠近0方式舍去。

    >>> dc.getcontext().rounding = dc.ROUND_05UP
    >>> round(dc.Decimal('1.51'), 1)
    Decimal('1.6')
    >>> round(dc.Decimal('1.01'), 1)
    Decimal('1.1')
    >>> round(dc.Decimal('1.17'), 1)
    Decimal('1.1')
    """


if __name__ == '__main__':
    dc.getcontext().rounding = dc.ROUND_HALF_UP
    print("round method ROUND_HALF_UP(4 off and 5 up)")
    print("dc.Decimal('1.245') = {}".format(round(dc.Decimal('1.245'), 2)))
