# coding: utf8

import re


def demo_reo_split():
    """
    split(string, maxsplit=0)
    使用模式匹配的子字符串，分解给出的字符串，返回包含各子串的列表。split方法可用于分割文本行。
    """
    rx = re.compile(r'[,;|\s*]\s*')             # []内的符号*视为非控制符
    print(rx.split('ac bd, ef* 123|456'))       # 使用各类间隔符的文本行, 分割内容（*和空格连接，都被视为分割符）
    # ['ac', 'bd', 'ef', '123', '456']


if __name__ == '__main__':
    demo_reo_split()
