# coding = utf8

import datetime
import pytz


def datetime_exp():
    """
    # 计算神州1号至神州2号发射时间之间有多少天
    >>> d1 = datetime.datetime(1999, 11, 20, 6, 30, 7)	# 神州1号发射时间
    >>> d2 = datetime.datetime(2001, 1, 10, 1, 0, 3)	# 神州2号发射时间
    >>> delta12 = d2 - d1                               # 之间相隔的时间（天数，秒数）
    >>> delta12
    datetime.timedelta(days=416, seconds=66596)
    >>> delta12.days
    416

    # 计算神州1号至神州2号发射时间之间有多少个周日
    >>> count = 0
    >>> for d in range(416):
    ...     dtt = d1 + datetime.timedelta(days=d)
    ...     if dtt.timetuple().tm_wday == 6:
    ...         count += 1
    >>> print(count)
    60

    # 使用pytz模块可以查找时区名称
    >>> pytz.all_timezones[0]
    'Africa/Abidjan'

    # 使用pytz模块的方法可以获取时区信息类型tzinfo对象
    >>> tz_utc = pytz.timezone('UTC')
    >>> tz_china_shanghai = pytz.timezone('Asia/Shanghai')
    >>> tz_china_chongqing = pytz.timezone('Asia/Chongqing')
    >>> tz_hawaii = pytz.timezone('US/Hawaii')

    # 创建一个无时区信息日期时间对象
    >>> dt = datetime.datetime(2022, 6, 7, 0, 0, 0)
    >>> print(dt)
    2022-06-07 00:00:00

    # 配置时区信息
    >>> dt_utc = dt.replace(tzinfo=tz_utc)
    >>> print(dt_utc)    # 设置为格林威治时间
    2022-06-07 00:00:00+00:00

    # 设置为中国上海时区时间，其中时区时差为8小时6分，并非标准北京时间
    >>> dt_shanghai = dt.replace(tzinfo=tz_china_shanghai)
    >>> print(dt_shanghai)
    2022-06-07 00:00:00+08:06

    # 为了避免当地时间的时间差，应使用本地化方法localize进行时区设置
    >>> dt_shanghai_loc = tz_china_shanghai.localize(dt)
    >>> print(dt_shanghai_loc)
    2022-06-07 00:00:00+08:00

    # 使用非本地化时区，转为目标时区日期时间，会带有当地日出时间差
    >>> print(dt_shanghai.astimezone(tz=tz_hawaii))
    2022-06-06 05:54:00-10:00

    # 使用本地化时区， 不会出现当地日出时间差
    >>> print(dt_shanghai_loc.astimezone(tz=tz_hawaii))
    2022-06-06 06:00:00-10:00
    """