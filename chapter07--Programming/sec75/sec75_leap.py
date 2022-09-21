# coding = utf8


def get_leap_year(beg_year=None, end_year=None):
    """
    公历的闰年
    计算从beg_year 到 end_year之间的闰年
    基于的原则：4年一闰，100年不闰，400年闰
    公元前年份：除4余数1的年份闰，除100余1的年份不闰，除400余1的年份闰
    闰年366天，平年365天
    :param beg_year: 开始年
    :param end_year: 结束年
    :return: 闰年年份列表
    >>> get_leap_year(1, 20)
    [4, 8, 12, 16, 20]
    >>> get_leap_year(-10, 10)
    [-9, -5, -1, 4, 8]
    """
    end_year = beg_year if end_year is None else end_year
    if end_year < beg_year:
        beg_year, end_year = end_year, beg_year
    leap = []
    for y in range(beg_year, end_year + 1):
        if y == 0:
            continue
        _y = y+1 if y < 0 else y
        if ((_y % 100) and (_y % 4 == 0)) | (_y % 400 == 0):
            leap.append(y)
    return leap


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
