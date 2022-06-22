# coding = utf8

import os


def traverse(pathname):
    """
    遍历一个目录，打印目录内的所有文件和目录名
    """
    pathfiles = os.listdir(pathname)
    print('[{}]'.format(pathname))	        # 打印当前目录及目录中的文件及子目录名
    for pf in pathfiles:
        print('\t{}'.format(pf))
    for d in pathfiles:		                # 递归遍历子目录
        if os.path.isdir(pathname+'/'+d):
            traverse(pathname + '/' + d)


if __name__ == '__main__':
    tdir = os.path.abspath('.')
    traverse(tdir)
