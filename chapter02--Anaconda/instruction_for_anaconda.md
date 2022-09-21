----------------
Anaconda 安装与使用
----------------
Anaconda是一个面向数据科学的Python计算环境集成管理平台。在提供基本集成包（7500+）的基础上，
使用本身的工具Conda管理独立环境。由于这些扩展包都经过了严格的版本兼容性测试，可以提供对科学计算和数据分析任务的强力支持。
Anaconda集成环境是最具代表性的Python产品，通过跟进Python官方的较新发布版本，集成了大量专业的软件包，在数据处理和分析领域深受用户青睐。

## 1. 安装

###（1） 登录网址<br>
官方网站：https://www.anaconda.com <br>
国内镜像: https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/

下载Anaconda时，需要注意操作系统类型和版本，例如，Windows64位环境，下载包名称应为：Anaconda3-2020.07-Windows-x86_64。

### (2) 下载
（1）运行下载的安装包<br>
（2）选择安装选项

安装Anaconda后，会建立一个类似Python安装包的Anaconda目录，其中存放Python解释器（Python.exe），
子目录Scripts中存放pip和conda，用于安装维护扩展包。Lib/site-packages中存放了安装的扩展包，
如IPython、Jupyter等，可以通过浏览查看安装了哪些扩展包。

### (3) 运行

(1) 命令行窗口运行<br>
如果安装中增加了路径环境变量，直接运行:<br>
`\> python` <br>
如果安装中没有设置路径环境变量，则需要进入Anaconda安装目录的scripts子目录:<br>
`scripts > python`

(2) Windows菜单<br>
在Windows菜单中，找到Anaconda项，点击有关子项。

(3) [Anaconda Powershell Prompt] Powershell命令行工具<br>
该工具提供基于命令行窗口的Python环境，在其中可以使用类似Linux的目录文件命令。

(4) [Anaconda Prompt] Prompt命令行工具<br>
该工具可以提供基于Windows命令行窗口的Python环境，在该窗口中使用Dos命令。

(5) [Jupyter Notebook] Jupyter工作簿。<br>
在浏览器中运行的集成开发环境，以单元为单位管理运行脚本。Notebook运行后，
会出现一个命令行窗口运行的系统状态，同时会在浏览器中启动编程界面。

(6)Spyder] 集成开发环境<br>
Spyder是一个比IDLE更专业化的代码编辑开发工具，最大的特点是提供了具有类似Matlab的“工作空间”，
从中可以方便地观察修改数组值。在窗口设置方面，Spyder沿袭了大多数代码编辑器的风格，
由代码窗口、工作空间窗口、控制台窗口构成，可以根据自己的喜好调整它们的位置和大小。
通过在编辑器中设置控制符，Spyder也实现了类似的单元式脚本管理。

## 2. [Anaconda Navigator] 导航台<br>
在Windows菜单中，找到Anaconda项，点击有关Anaconda Navigator子项。

## 3. 使用conda管理运行环境

conda是Anaconda配置的环境管理工具，具有丰富的管理功能，包括查看、下载、更新Python第三方包等。

conda is a tool for managing and deploying applications, environments and packages.


##`usage: conda-script.py [-h] [-V] command ...`


### Options:

### positional arguments:

### command

clean&emsp; &emsp; &emsp; &emsp; Remove unused packages and caches.<br>
compare&emsp; &emsp; &emsp; &emsp; Compare packages between conda environments.<br>
config&emsp; &emsp; &emsp; &emsp;  Modify configuration values in .condarc. This is modeled after the git config command. Writes to the
user .condarc file (C:\Users\admin\.condarc) by default.<br>
create&emsp; &emsp; &emsp; &emsp;  Create a new conda environment from a list of specified packages.<br>
help&emsp; &emsp; &emsp; &emsp;  Displays a list of available conda commands and their help strings.<br>
info&emsp; &emsp; &emsp; &emsp;  Display information about current conda install.<br>
init&emsp; &emsp; &emsp; &emsp;  Initialize conda for shell interaction. [Experimental]<br>
install&emsp; &emsp; &emsp; &emsp; Installs a list of packages into a specified conda environment.<br>
list&emsp; &emsp; &emsp; &emsp;  List linked packages in a conda environment.<br>
package&emsp; &emsp; &emsp; &emsp; Low-level conda package utility. (EXPERIMENTAL)<br>
remove&emsp; &emsp; &emsp; &emsp;  Remove a list of packages from a specified conda environment.<br>
uninstall &emsp; &emsp; &emsp; &emsp; Alias for conda remove.<br>
run&emsp; &emsp; &emsp; &emsp;   Run an executable in a conda environment. [Experimental]<br>
search&emsp; &emsp; &emsp; &emsp;  Search for packages and display associated information. The input is a MatchSpec, a query language
for conda packages. See examples below.<br>
update&emsp; &emsp; &emsp; &emsp;  Updates conda packages to the latest compatible version.<br>
upgrade&emsp; &emsp; &emsp; &emsp; Alias for conda update.

### optional arguments:<br>
-h, --help     Show this help message and exit.<br>
-V, --version  Show the conda version number and exit.

###conda commands available from other packages:<br>
build<br>
content-trust<br>
convert<br>
debug<br>
develop<br>
env<br>
index<br>
inspect<br>
metapackage<br>
pack<br>
render<br>
repo<br>
server<br>
skeleton<br>
token<br>
verify<br>
