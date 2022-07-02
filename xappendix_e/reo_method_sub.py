# coding: utf8

import re


def demo_findall():
    """
    sub(repl, string, count=0)
    使用子串repl对string内的匹配串进行替换。

    >>> import re
    >>> ro = re.compile('abc')
    >>> ro.sub('aaa', 'abcddabcdd')
    'aaaddaaadd'
    """
