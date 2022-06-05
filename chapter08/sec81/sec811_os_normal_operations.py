# coding = utf8

import os


def test_os_op():
    """
    实现目录基本操作示例：
    >>> os.mkdir('temp_path')		# 创建子目录
    >>> os.cddir('temp_path')		# 进入子目录
    >>> os.chdir('..')		                    # 进入上一级目录
    >>> os.rename('temp_path', 'temp_new_path')	# 将子目录mypath改名为newpath
    >>> os.rmdir('temp_new_path')		        # 删除子目录
    >>> os.makedirs('temp_path2/path2/p3')	    # 创建多级子目录
    >>> os.removedirs('temp_path2/path2/p3')	# 删除多级子目录，要求各级目录都为空目录

    实现文件更名、删除操作示例：
    >>> os.rename(src='temp_file.txt', dst='temp_file2.txt')	# 文件更名（需要保证更名前不存在文件dst）
    >>> os.remove('temp_file2.txt')			                    # 删除文件
    >>> os.path.isfile('temp_file2.txt')			            # 判断文件是否存在
    False
    >>> os.rename(src='temp_dir', dst='temp_new_dir')	        # 更改目录名（需要保证更名前不存在目录dst）
    >>> os.path.isdir('temp_new_dir')			                # 判断目录是否存在
    True
    >>> os.removedirs('temp_new_dir')
    """
