# coding = utf8

import os


def get_dirtree_by_walk(pathname, sort=False):
    """
    生成目录结构树形。 根据节点层级生成'| '间隔符，节点项前为 '|--'
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
        ps = '{}{} [dir] [files:{} dirs:{}]'.format(indent, os.path.split(root)[1], len(files), len(dirs))
        dir_tree += ps + '\n'
        for file in files:
            indent = '| ' * (level_num + 1) + '|--'
            dir_tree += '{}{}\n'.format(indent, file)
    return dir_tree


if __name__ == '__main__':
    tdir = os.path.abspath('..')
    print(get_dirtree_by_walk(tdir))
