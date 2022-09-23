# coding = utf8

from string import punctuation as ep
from zhon.hanzi import punctuation as hp

cp = hp[-4] + hp[:12] + hp[-1] + hp[12:18] + hp[-3] + hp[18:29]
table_to_chinese = str.maketrans({ec: hc for ec, hc in zip(ep, cp)})
table_to_english = str.maketrans({ec: hc for ec, hc in zip(cp, ep)})


def punc_swop(raw_str, to_chinese=True):
    """
    转换中英文标点
    :param raw_str(str): 源文本字符串
    :param to_chinese(bool): True-转为中文标点，False-转为英文标点
    :return: str 返回转换后的字符串

    >>> es = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
    >>> punc_swop(es)
    '！＂＃＄％＆＇（）＊＋，－。／：；＜＝＞？＠［＼］＾＿｀｛｜｝～'
    >>> punc_swop(punc_swop(es), to_chinese=False)
    '!"#$%&\\'()*+,-./:;<=>?@[\\\\]^_`{|}~'
    """
    table = table_to_chinese if to_chinese else table_to_english
    return raw_str.translate(table)


def file_punc_swop(from_file, to_file, to_chinese=True, encoding='utf8'):
    """
    将文件中的标点符号转换
    :param from_file 源文本文件 source text file
    :param to_file 目标文件 target text file
    :to_chinese(str) True: 转换为中文标点 from en to cn, False: 转换为英文标点 from cn to en
    :encoding(str) 编码字符集名称


    >>> en_punc = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
    >>> with open('temp_punc_en.txt', 'w') as fp:
    ...    fp.write(en_punc)
    32
    >>> file_punc_swop('temp_punc_en.txt', 'temp_punc_cn.txt')	    # 将文件temp.txt中的英文标点转为汉语标点
    >>> with open('temp_punc_cn.txt', encoding='utf8') as fp:
    ...     print(fp.read())
    ！＂＃＄％＆＇（）＊＋，－。／：；＜＝＞？＠［＼］＾＿｀｛｜｝～
    """
    with open(from_file, 'r', encoding=encoding) as f1, \
            open(to_file, 'w', encoding=encoding) as f2:
        for line in f1:
            f2.write(punc_swop(line, to_chinese))
