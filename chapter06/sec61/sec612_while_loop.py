# coding: utf8


a = 2
while a >= 1:
    print(a)
    a -= 1
else:
    print('bye1')   # else语句被执行

while a > -2:       # 符合 a > -2 时执行循环语句
    print(a)        # 循环体语句开始
    a = a - 1
    if a < 0:       # 中断循环的条件
        break       # 执行break中断退出循环
else:
    print('bye2')   # else语句未执行

a = 0
while a > 0:        # 因a > 0为False，循环不执行
    print(a)
    a = a - 1
    break
else:
    print('bye3')   # else语句被执行
