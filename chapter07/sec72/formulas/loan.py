# coding = utf8

from collections import namedtuple


def repay(b, y, r, mode=1):
    """
    按贷款总额、利率、年限、方式，进行月还款与利息计算

    :parameter
    :param b:float 贷款总额
    :param y:int 还款年数，正整数
    :param r:float 年利率
    :param mode:int 还款方式，1--等额本金， 2--等额本息

    :return：namedtuple,
    (month_repay: list, total_repay: float, total_interest: float)
    (月还款，总还款，总利息)

    >>> r1 = repay(2000000, 30, 0.049, mode=1)    # 使用等额本息方式
    >>> round(r1.month_repay[0], 2)
    13722.22
    >>> round(r1.total_repay, 2)
    3474083.33
    >>> round(r1.total_interest, 2)
    1474083.33
    >>> r2 = repay(2000000, 30, 0.049, mode=2)    # 使用等额本息方式
    >>> format(r2.month_repay[0], '.2f')
    '10614.53'
    """
    # 还款月数、月息
    m = y * 12
    mr = r / 12
    # 计算月还款
    if mode == 1:
        # 等额本金方式每月本金、利息、还款
        month_principle = [b/m] * m
        month_interest = [(b - b/m * j) * mr for j in range(m)]
        month_repay = [x+y for x, y in zip(month_principle, month_interest)]
    elif mode == 2:
        # 等额本息方式月还款
        month_repay = [(b * mr * (1 + mr) ** m) / ((1 + mr) ** m - 1)] * m
    else:
        # 无效模式
        raise ValueError('Invalid Mode: {}'.format(mode))
    # 总还款
    total_repay = sum(month_repay)
    # 总利息
    total_interest = total_repay - b
    # 计算结果的命名元祖
    Result = namedtuple('Result', ('month_repay', 'total_repay', 'total_interest'))
    return Result(month_repay, total_repay, total_interest)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
