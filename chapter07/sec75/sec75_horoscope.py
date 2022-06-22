# coding = utf8

import datetime
import zhdate


def get_horoscope(month, day):
    """
    根据公历生日的月份和日期，计算星座
    >>> get_horoscope(8, 13)
    '狮子'
    >>> get_horoscope(12, 23)
    '魔羯'
    """
    holoscope = ['魔羯', '水瓶', '双鱼', '牡羊', '金牛', '双子', '巨蟹',
                 '狮子', '处女', '天秤', '天蝎', '射手']
    cutoff_day = (20, 19, 21, 21, 21, 22, 23, 23, 23, 23, 22, 22)
    next_month = 1 if day < cutoff_day[month - 1] else 0
    _month = month - next_month
    return holoscope[_month if _month<12 else 0]


def get_horoscope2(month, day):
    """
    根据公历月份和日期，计算星座
    >>> get_horoscope2(8, 13)
    '狮子'
    >>> get_horoscope2(1, 12)
    '魔羯'
    >>> get_horoscope2(12, 23)
    '魔羯'
    """
    holoscope = ['魔羯', '水瓶', '双鱼', '牡羊', '金牛', '双子', '巨蟹',
                 '狮子', '处女', '天秤', '天蝎', '射手']
    cutoff_day = (20, 19, 21, 21, 21, 22, 23, 23, 23, 23, 22, 22)
    _month = month - (1 if day < cutoff_day[month - 1] else 0)
    return holoscope[_month if _month<12 else 0]


def get_horoscope3(month, day):
    """
    根据公历月份和日期，计算星座
    >>> get_horoscope3(8, 13)
    '狮子'
    >>> get_horoscope3(12, 23)
    '魔羯'
    """
    pos = month - (1 if day < (int("102223444433"[month-1:month])+19) else 0)
    return "魔羯水瓶双鱼牡羊金牛双子巨蟹狮子处女天秤天蝎射手魔羯"[pos*2:pos*2+2]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
