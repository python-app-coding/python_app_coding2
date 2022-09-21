# coding: utf8

"""
>>> import time

# 返回本地时间（struct_time）
>>> t1 = time.localtime()
>>> print(t1)
time.struct_time(tm_year=2022, tm_mon=6, tm_mday=6, tm_hour=7, tm_min=9, tm_sec=8, tm_wday=0, tm_yday=157, tm_isdst=0)
>>> t1.tm_zone
'中国标准时间'
>>> t1.tm_gmtoff
28800

# 返回格林威治时间(struct_time）
>>> time.gmtime()
time.struct_time(tm_year=2022, tm_mon=6, tm_mday=5, tm_hour=23, tm_min=9, tm_sec=8, tm_wday=6, tm_yday=156, tm_isdst=0)

time.ctime()返回的时间格式为ctime格式字符串时间。
# 返回字符串格式的当前时间(ctime格式)
>>> time.ctime()
'Mon Jun  6 07:11:40 2022'

>>> def count_time():
...      start = time.time()
...      a = sum(range(100000))
...      c = time.time() - start
...      print('consumed time = {:.4f}'.format(c))
>>> count_time()	# 由于执行过程会有优化，多次调用时，后面的会小一些
consumed time = 0.0030

# 一个模拟耗费时间的函数
>>> def do_something(secs=1):
...     time.sleep(secs)

# 测试执行do_something耗费的时间
>>> def count_time():
...     start = time.time()
...     do_something(0.1)
...     c = time.time() - start
...     print('consumed time = {:.4f}'.format(c))
>>> count_time()	# 实际结果可能会稍大一些
consumed time = 0.1060

# 格式化成为日期时间形式
>>> time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
'2022-07-03 22:44:56'

# 格式化成ctime形式
>>> time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
'Sun Jul 03 22:47:17 2022'
"""