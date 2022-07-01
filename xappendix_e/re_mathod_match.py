# coding: utf8

import re


def demo_match():
    # 返回匹配对象
    r = re.match('[0-9]{4}-[0-9]{8}','0531-81293555 is a phone No.')
    print(r)
    # <re.Match object; span=(0, 13), match='0531-81293555'>

    # 在匹配中使用标志flags设置，可以改变匹配方式。
    # 使用re.A忽略非ASCII字符:
    r = re.match('(\w*)', '编码', flags=re.A)
    print(r)
    # <re.Matchobject; span=(0, 0), match=''>    # 不匹配非ASCII字符

    r = re.match('(\w*)', 'abc', flags=re.A)
    print(r)
    # <re.Matchobject; span=(0, 3), match='abc'>    # 匹配ASCII字符

    r = re.match('(\w*)', 'abc编码', flags=re.A)
    print(r)
    # <re.Matchobject; span=(0, 3), match='abc'>    # 不匹配非ASCII字符

    r = re.match('(\w*)', 'abc编码', flags=re.U)
    print(r)
    # <re.Matchobject; span=(0, 5), match='abc编码'>    # 匹配所有Unicode字符

    # 使用re.I忽略大小写：
    r = re.match('(\w+) (?P<number>[0-9]+)','Week 03 is next', flags=re.I)
    print(r)

    # <re.Matchobject; span=(0, 7), match='week 03'>    # 忽略大小写进行匹配

    # 使用re.M多行模式，按多行字符处理：
    r = re.match('foo.$', 'foo1\nfoo2\n', flags=re.M)
    print(r)
    # <re.Matchobject; span=(0, 7), match='foo1'>   # 多行模式匹配第一个换行符前的串
    
    r = re.search('foo.$', 'foo1\nfoo2\n')
    print(r)
    # <re.Match object; span=(5, 9), match='foo2'>  # 非多行模式匹配最后的换行符前的串

    # 使用re.S匹配所有字符：
    r = re.match('.*', 'abc\n编码', flags=re.S)
    print(r)
    # <re.Matchobject; span=(0, 6), match='abc\n编码'>

    # 使用re.X忽略空格、注释（注意，不能使用tab字符）：
    r = re.match(r"""\d+  	    # 整数部分
            \.                  # 小数点
            \d*                 # 小数点后数字""",
            '123.789',
            flags=re.X)
    print(r)
    # < re.Matchobject; span = (0, 7), match = '123.789' >

    # 使用非注解方式，匹配结果相同
    r = re.match(r"\d+\.\d*", '123.789')
    print(r)
    # < re.Matchobject; span = (0, 7), match = '123.789' >


if __name__ == '__main__':
    demo_match()
