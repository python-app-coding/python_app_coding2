=================
构建Python基本环境
=================
---------------
下载Python开发包
---------------
###1. 下载
   
官方网站：http://python.org

选择版本

Windows：
1. embeded version 绿色版本，仅包含解释器和少量工具
2. source pakcage 源码包，下载后解压编译
3. install pakcage 运行安装包，下载后运行或直接运行

4. 下载开发包

###2.安装











---------------------
使用pip下载安装第三方包
---------------------

# pip update to specific version
pip install -U package==x.x.x
pip install --upgrade psycopg2==2.7.5

# 国内常用的镜像网站
# pip from tsinghua, aliyun
pip install [package] -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install [package] -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com


# set default source
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple


## set pip.ini
[global]
timeout=40
index-url=https://pypi.tuna.tsinghua.edu.cn/simple/
extra-index-url=
        http://mirrors.aliyun.com/pypi/simple/
        http://pypi.douban.com/simple
        http://pypi.mirrors.ustc.edu.cn/simple/

[install]
trusted-host=
        pypi.tuna.tsinghua.edu.cn
        mirrors.aliyun.com
        pypi.douban.com
        pypi.mirrors.ustc.edu.cn

