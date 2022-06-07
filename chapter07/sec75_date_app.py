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


class ChinaEra:
    """
    功能： 计算年月日时天干地支
    限制： 阴历只支持1901年之后的日期
    依赖： zhdate, 该模块使用香港天文台数据推算阴历和公历转换

    >>> ChinaEra().get_china_era(1976, 8, 3, 12, True)
    {'年': '丙辰', '月': '丁酉', '日': '乙酉', '时': '丙午', '周': '五', '属': '龙'}
    """

    gan = '甲乙丙丁戊己庚辛壬癸'
    zhi = "子丑寅卯辰巳午未申酉戌亥"
    shu = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
    week = '一二三四五六日'

    def __init__(self, year=1900, month=1, day=1, hour=0, lunar=True):
        """
        接收年(year)月(month)日(day)时(hour)，
        lunar==True: 阴历, lunar==False: 公历
        设置lunar=False时，输入公历参数，系统将公历日期转换为阴历日期，再计算天干地支
        计算天干地支值：china_era(dict)
        """
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.lunar = lunar
        if not lunar:
            self.year, self.month, self.day = self.get_china_date_from_solar_date(year, month, day)
            self.lunar = True
        self.china_era = self.get_china_era(self.year, self.month, self.day, self.hour, True)

    def __str__(self):
        return str(self.china_era)

    def get_china_era(self, year=None, month=1, day=1, hour=0, lunar=True):
        """
        计算年月日时的天干地支及周天、属相
        根据lunar判断所提供日期的阴历、公历
        :param hour: float, 0-23.99
        :param year: int
        :param month: int, 1-12
        :param day: int, 1-31
        :param lunar: bool, True:阴历, False: 公历
        :return: dict，年月日时的回天干地支及周天、属相
        >>> ChinaEra().get_china_era(2020, 9, 13, 1, False)
        {'年': '庚子', '月': '甲申', '日': '丁丑', '时': '庚子', '周': '日', '属': '鼠'}
        >>> ChinaEra().get_china_era(2020, 8, 15, 19, True)
        {'年': '庚子', '月': '乙酉', '日': '丁酉', '时': '庚酉', '周': '四', '属': '鼠'}
        """
        # use date from parameters
        if isinstance(year, int):
            if not lunar:
                self.year, self.month, self.day = ChinaEra.get_china_date_from_solar_date(year, month, day)
            else:
                self.year = year
                self.month = month
                self.day = day
                self.hour = hour
        year_gz = self.get_china_era_year(self.year)
        month_gz = self.get_china_era_month(self.year, self.month)
        day_gz = self.get_china_era_day(self.month, self.day)
        hour_gz = self.get_china_era_hour(self.month, self.day, self.hour)
        self.china_era = dict({'年': year_gz, '月': month_gz, '日': day_gz, '时': hour_gz,
                               '周': self.get_week_day(self.year, self.month, self.day, lunar=self.lunar),
                               '属': self.shu[self.zhi.find(year_gz[1])]
                               })
        return self.china_era

    def get_week_day(self, year=None, month=-1, day=-1, lunar=False):
        """
        接收公历年月日，返回周天的汉字字符串
        如果lunan=True，则将系统自动将阴历转换为公历，再计算周天
        :param year: int
        :param month: int, 1-12
        :param day: int, 1-31
        :param lunar: bool, True:阴历, False: 公历
        :return: week_day_chinese_no
        >>> ChinaEra().get_week_day(2020, 8, 15, lunar=True)
        '四'
        """
        if not all([isinstance(year, int), 1 <= month <= 12, 1 <= day <= 31]):
            year = self.year
            month = self.month
            day = self.day
            year, month, day = ChinaEra.get_solar_date_from_china_date(year, month, day)
        else:
            if lunar:
                year, month, day = ChinaEra.get_solar_date_from_china_date(year, month, day)
        week_day_no = datetime.datetime(year=year, month=month, day=day).weekday()
        return self.week[week_day_no]

    def get_china_era_year(self, year):
        """
        根据某年的干支数，分别推算干支
        本函数是以2000年的干（6）支（4）为基点，向前或向后推算
        >>> ChinaEra().get_china_era_year(2020)
        '庚子'
        >>> ChinaEra().get_china_era_year(1998)
        '戊寅'
        """
        # y2000_gan = 6, y2000_zhi = 4
        y_gan = (6 + (year - 2000) % 10) % 10
        y_zhi = (4 + (year - 2000) % 12) % 12
        return self.gan[y_gan:y_gan+1]+self.zhi[y_zhi:y_zhi+1]

    def get_china_era_month(self, year, month):
        """
        计算月份天干地支
        天干：年份后两位加2后乘以2再加月份数，再取10的余数为天干
        地支：月份数+2，大于12则-12
        :param year:int
        :param month:int 1-12
        :return （gan+zhi):str
        >>> ChinaEra().get_china_era_month(2015, 5)
        '壬午'
        """
        gan_month = ((year % 100 + 2) * 2 + month - 1) % 10
        return self.gan[gan_month] + self.zhi[(month+2-1) % 12]

    def get_china_era_day(self, month, day):
        """
        计算日的天干地支
        >>> ChinaEra().get_china_era_day(7, 13)
        '甲子'
        """
        if month not in range(1, 13) or day not in range(1, 32):
            raise ValueError
        # gan = '甲乙丙丁戊己庚辛壬癸'
        # zhi = "子丑寅卯辰巳午未申酉戌亥"
        base = [47, 18, 46, 17, 47, 18, 48, 19, 50, 20, 51, 21]
        base1 = day + base[month-1]
        gan_no = (base1-1) % 10
        zhi_no = (base1-1) % 12
        return self.gan[gan_no] + self.zhi[zhi_no]

    def get_china_era_hour(self, month, day, hour):
        """
        计算时辰的天干地支
        >>> ChinaEra().get_china_era_hour(7, 13, 4)
        '甲寅'
        """
        day_gz = self.get_china_era_day(month, day)
        day_gan_pos = self.gan.find(day_gz[0])
        day_gan_pos = day_gan_pos if day_gan_pos < 5 else day_gan_pos - 5
        day_gan = self.gan[day_gan_pos]
        hour_gan_dict = {'甲': 0, '乙': 2, '丙': 4, '丁': 6, '戊': 8}
        hour_gan = self.gan[hour_gan_dict[day_gan]]
        hour_zhi_no = 0
        if not(23 < hour <= 24 or 0 <= hour <= 1):
            for i in range(11):
                if i*2 + 1 < hour <= (i+1)*2 + 1:
                    hour_zhi_no = i + 1
        hour_zhi = self.zhi[hour_zhi_no:][0]
        return hour_gan+hour_zhi

    @staticmethod
    def get_china_date_from_solar_date(year, month, day):
        """
        将公历日期转换为阴历
        只支持1900-2100年
        :param year: int 1900-2100
        :param month:int 1-12
        :param day: int 1-30
        :return: tuple, (year, month, day)
        >>> ChinaEra.get_china_date_from_solar_date(2020, 10, 1)
        (2020, 8, 15)
        """
        # import zhdate
        ln = zhdate.ZhDate.from_datetime(datetime.datetime(year, month, day))
        return ln.lunar_year, ln.lunar_month, ln.lunar_day

    @staticmethod
    def get_solar_date_from_china_date(year, month, day, leap=False):
        """
        将阴历日期转换为公历
        只支持1900-2100年
        使用leap指明所给定的month是否为闰月
        :param year: lunar
        :param month: lunar
        :param day: lunar
        :param leap: bool, 是否为闰月
        :return: calendar year, month, day
        >>> ChinaEra.get_solar_date_from_china_date(2020, 8, 15)
        (2020, 10, 1)
        """
        # import zhdate
        solar_date = zhdate.ZhDate(year, month, day, leap).to_datetime()
        return solar_date.year, solar_date.month, solar_date.day


def get_china_era_year(year):
    """
    计算某年的干支
    以2000年的干（6）支（4）为基点，向前或向后推算
    >>> get_china_era_year(2020)
    '庚子'
    >>> get_china_era_year(1998)
    '戊寅'
    """
    gan = '甲乙丙丁戊己庚辛壬癸'
    zhi = "子丑寅卯辰巳午未申酉戌亥"
    # y2000_gan = 6, y2000_zhi = 4
    y_gan = (6 + (year - 2000) % 10) % 10
    y_zhi = (4 + (year - 2000) % 12) % 12
    return gan[y_gan:y_gan+1]+zhi[y_zhi:y_zhi+1]


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
