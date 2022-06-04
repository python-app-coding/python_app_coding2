# coding = utf8


def fun_add(*args):
    return sum(args)


def compound_score(*args):
    """
    计算合成分数
    :param args: tuple[(score, coefficient)]
    :return: compound score
    >>> compound_score((90, 0.5),(80, 0.3),(85, 0.2))
    86.0
    """
    return sum([x[0] * x[1] for x in args])  # 使用列表推导式可以提供更为简化的代码


def fun_paras(x, y, z, k1=1, k2=30):
    """
    演示参数设置与调用
    三个位置参数，2个关键字参数，位置参数必须在前面
    :param x:
    :param y:
    :param z:
    :param k1:
    :param k2:
    :return:
    >>> x, y, z = 1, 2, 3
    >>> fun_paras(y, x, z, k2=100)  # 使用关键字参数的缺省值，关键字参数可以忽略位置
    (2, 1, 3, 1, 100)
    """
    return x, y, z, k1, k2


def fun_any_paras(*args, **kargs):  # 接收任意数量位置参数，任意个数的关键字参数
    """

    :param args:
    :param kargs:
    :return:
    >>> fun_any_paras(1, 2, a=1, b=2)  # 任意指定位置和关键字参数，位置参数必须都在前面！
    (1, 2)
    {'a': 1, 'b': 2}
    """
    print(args)
    print(kargs)


def com_score(*args):
    """
    计算综合分数
    :parameter 参数
    *args: 不确定个数的元组（float, float）, 各科目分数及合成系数
    :return 返回值
    score: float, 合成分数

    >>> com_score((100, 0.3), (80, 0.7))
    86.0
    """
    from operator import mul
    return sum(mul(*x) for x in args)


def com_score_art(uni_score, art_score, subject='文编', ndigits=2):
    """
    计算艺术综合分数
    subject：str，值域={"美术"，“文编”， “播音”，“书法”，“舞蹈”}
    uni_score: float, 统一考试分数
    art_score：float, 艺术专业分数
    ndigits: 保留小数位数，缺省值=2. 使用Python内置的舍人函数round， 与四舍五入方式不同

    >>> com_score_art(451, 200, subject='美术')
    '275.30'
    >>> com_score_art(170.5, 10, subject='美术', ndigits=1)
    '58.2'
    >>> com_score_art(5, 10, subject='美术', ndigits=0)
    '9'
    """
    # 各类别系数
    props = {
         '文编': (0.7, 0.3),
         '播音': (0.7, 0.3),
         '美术': (0.3, 0.7),
         '舞蹈': (0.3, 0.7),
         '书法': (0.4, 0.6)
         }
    # 合成分数
    com_socre = sum(x * y for x, y in zip((uni_score, art_score), props[subject]))
    # 返回字符串，保留nidigits位小数位
    return format(com_socre, '.{}f'.format(ndigits))


def com_score_art_round45(unitest_score, art_score, subject='文编', ndigits=2):
    """

    :param unitest_score:
    :param art_score:
    :param subject:
    :param ndigits:
    :return:

    >>> com_score_art_round45(451, 200, subject='美术')
    '275.30'
    >>> com_score_art_round45(170.5, 10, subject='美术', ndigits=1)
    '58.2'
    >>> com_score_art_round45(5, 10, subject='美术', ndigits=0)
    '9'
    """
    # 使用高精度十进制计算模块和四舍五入方式
    import decimal
    decimal.getcontext().rounding = decimal.ROUND_HALF_UP
    # 各类别系数
    D = decimal.Decimal
    r03, r07, r04, r06 = D('0.3'), D('0.7'), D('0.4'), D('0.6')
    props = {
        '文编': (r07, r03),
        '播音': (r07, r03),
        '美术': (r03, r07),
        '舞蹈': (r03, r07),
        '书法': (r04, r06)
        }
    # 合成分数
    comp_socre=sum(D(x)*ratio for x, ratio in zip((unitest_score, art_score), props[subject]))
    # 使用 ROUND_HALF_UP 方式进行舍入（四舍五入）
    comp_socre = round(comp_socre, ndigits)
    # # 返回字符串，保留 nidigits 位小数位
    return str(comp_socre)
