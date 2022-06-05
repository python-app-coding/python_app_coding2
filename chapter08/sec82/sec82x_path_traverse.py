# -*- coding: utf-8 -*-

"""
使用os.listdir，os.walk,通过遍历生成目录树，
create path-files tree through traverse path with os.listdir or os.walk
Author: Wang Xichang
Date: 2015-09-18
"""


from sys import argv

import os


def traverse_dir(path):
    """
    遍历一个目录，打印目录内的所有文件和目录名
    travers a path to print all files and path name

    :param path: path to traverse
    :return:
    """
    print('[{}]'.format(path))          # 打印当前目录及目录中的文件及子目录名
    pathfiles = os.listdir(path)
    for pf in pathfiles:
        print('\t{}'.format(pf))
    for d in pathfiles:                 # 递归遍历子目录
        if os.path.isdir(path+'/'+d):
            traverse_dir(path+'/'+d)


def get_dirtree_by_listdir(pathname, include_dir=None, include_files=None, sort=False, indent_level=0):
    """
    使用os.listdir方法生成目录结构树形。
    根据节点层级生成'| '间隔符，节点项前为 '|--'
    ：pathname 开始遍历的根目录
    ：sort 是否对目录内容项进行排序
    返回目录树文本行
    """
    dir_tree = ''
    cur_files = os.listdir(pathname)
    if include_files:
        cur_files = [f for f in cur_files if f in include_files or f in include_dir]
    if sort:
        cur_files = sorted(cur_files)
    files = [f for f in cur_files if not os.path.isdir(pathname+'/'+f)]
    dirs = [d for d in cur_files if os.path.isdir(pathname+'/'+d)]
    indent = '| ' * indent_level + '|--'
    ps = '{}{} [path] [files:{} dirs:{}]'.format(indent, os.path.split(pathname)[1], len(files), len(dirs))
    dir_tree += ps + '\n'
    indent = '| ' * (indent_level + 1) + '|--'
    for file in files:
        dir_tree += '{}{}\n'.format(indent, file)
    for dr in dirs:
        if include_dir:
            if dr not in include_dir:
                continue
        dir_tree += get_dirtree_by_listdir(pathname + '/' + dr,
                                           include_dir=include_dir,
                                           include_files=include_files,
                                           sort=sort,
                                           indent_level=indent_level + 1)
    return dir_tree


def get_dirtree_by_walk(pathname, sort=False):
    """
    使用os.walk方法生成目录结构树形。
    根据节点层级生成'| '间隔符，节点项前为 '|--'
    ：pathname 开始遍历的根目录
    ：sort 是否对目录内容项进行排序
    返回目录树文本行
    """
    dir_tree = ''
    for root, dirs, files in os.walk(pathname):
        if sort:
            dirs = sorted(dirs)
            files = sorted(files)
        level_num = root.replace(pathname, '').count(os.sep)
        indent = '| ' * level_num + '|--'
        ps = '{}{} [path] [files:{} dirs:{}]'.format(indent, os.path.split(root)[1], len(files), len(dirs))
        dir_tree += ps + '\n'
        for file in files:
            indent = '| ' * (level_num + 1) + '|--'
            dir_tree += '{}{}\n'.format(indent, file)
    return dir_tree


def get_dirtree(pathname='.', sort=False, include_dir=None, include_files=None):
    """
    使用中文制表符生成目录树 use china table char
    \u2500:─, \u2514:└, \u251c:├, \u2502:│
    \u25cf:●, \u25ce:◎
    :param pathname: path name
    :param sort: sort pathname
    :param include_dir: list of str,  set paths that is included in pathname
    :param include_files: list of str,  set files that is included in pathname
    :return:
    """
    # include = [] if not include_dir else include_dir
    dir_text = get_dirtree_by_listdir(pathname, include_dir=include_dir, include_files=include_files, sort=sort)
    # print(dir_text)

    # remove left char and replace to China tab char
    dir_text_new = ''
    for line in dir_text.split('\n'):
        if len(line) == 0: # or all([ix not in line for ix in include]):
            continue
        line_new = line
        for i in range(0, len(line), 2):
            if line[i:i+2] == '| ' and line[i+2:i+5] == '|--':
                line_new = ' '*(int(i/2)+1)*2 + '\u2514' + '\u2500' + line[i+2+3:]
                break
        dir_text_new += line_new + '\n'
    # print(dir_text_new)

    # set table char
    dir_text_new2 = ''
    lines = [line for line in dir_text_new.split('\n') if len(line) > 0]
    for line_num, line in enumerate(lines):
        if line_num == 0:
            # set char: ●─◎─ for root node
            line_new = '\u25cf\u2500\u25ce\u2500' + line[3:] + '\n'
        elif ('\u2514' in line) and ('[path]' not in line) and (line_num < len(lines)-1):
            # set start char to '├' for ch3file item
            line_new = line.replace('\u2514', '\u251c') + '\n'
        else:
            if '[path]' in line:
                # set start char to '└─◎' for path
                line_new = line.replace('\u2514', '\u2514\u2500\u25ce') + '\n'
            else:
                line_new = line + '\n'
        dir_text_new2 += line_new

    # set ├ to └ for last ch3file in subdir
    dir_text = ''
    lines = [line for line in dir_text_new2.split('\n') if len(line) > 0]
    for li, line in enumerate(lines):
        line_new = line + '\n'
        if li < len(lines)-1:
            if line.lstrip()[0] == '\u251c':                # ├
                if lines[li+1].lstrip()[0] == '\u2514':     # └
                    if line.find('\u251c') != lines[li+1].find('\u2514'):
                        line_new = line.replace('\u251c', '\u2514') + '\n'
        dir_text += line_new

    # add vertical char
    lines = [line for line in dir_text.split('\n') if len(line) > 0]
    for li in range(len(lines)-1, 0, -1):
        dirpos = findn(lines[li], '\u2514')
        if len(dirpos) > 0:
            for j in range(li-1, 0, -1):
                for p in dirpos:
                    if p > len(lines[j]) - 1:
                        continue
                    if lines[j][p] == ' ':
                        lines[j] = lines[j][0:p] + '\u2502' + lines[j][p + 1:]
                    else:
                        dirpos.remove(p)
                        break
    dir_text = '\n'.join(lines)

    return dir_text


def findn(string, sub):
    """
    定位当前行目录标识符的开始位置
    :param string:
    :param sub:
    :return:
    """
    result = []
    _str = string
    _pos = 0
    while True:
        if sub in _str:
            pos = _str.find(sub)
            result += [pos+_pos]
            _pos += pos + 1
            _str = _str[pos+1:]
        else:
            return result


def get_dir_files(pathname, suff_list=None):
    """
    遍历一个目录，打印目录内的所有文件和目录名
    :param pathname: 路径名称
    :param suff_list: 后缀名称
    """
    suff_list = [] if not suff_list else suff_list
    # print('[{}]'.format(pathname))
    pathfiles = os.listdir(pathname)
    for pf in [f for f in pathfiles if f[f.find('.'):] in suff_list]:
        print('\t{}'.format(pathname + '/' + pf))
    for d in pathfiles:
        if os.path.isdir(pathname+'/'+d):
            get_dir_files(pathname + '/' + d, suff_list)    # 递归子目录


if __name__ == '__main__':
    # get path-tree for command line: python argv[1]
    path = os.path.abspath('../..')
    if len(argv) > 1:
        path = argv[1]
    print(path)
    print('get path-tree by os.listdir:')
    print(get_dirtree_by_listdir(path))
    print('get path-tree by os.walk:')
    print(get_dirtree_by_walk(path))
    print('get path-tree:{}'.format(path))
    print(get_dirtree(path))
