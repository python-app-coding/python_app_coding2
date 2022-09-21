----------------
Anaconda ��װ��ʹ��
----------------
Anaconda��һ���������ݿ�ѧ��Python���㻷�����ɹ���ƽ̨�����ṩ�������ɰ���7500+���Ļ����ϣ�
ʹ�ñ���Ĺ���Conda�������������������Щ��չ�����������ϸ�İ汾�����Բ��ԣ������ṩ�Կ�ѧ��������ݷ��������ǿ��֧�֡�
Anaconda���ɻ�������ߴ����Ե�Python��Ʒ��ͨ������Python�ٷ��Ľ��·����汾�������˴���רҵ��������������ݴ���ͷ������������û�������

## 1. ��װ

###��1�� ��¼��ַ<br>
�ٷ���վ��https://www.anaconda.com <br>
���ھ���: https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/

����Anacondaʱ����Ҫע�����ϵͳ���ͺͰ汾�����磬Windows64λ���������ذ�����ӦΪ��Anaconda3-2020.07-Windows-x86_64��

### (2) ����
��1���������صİ�װ��<br>
��2��ѡ��װѡ��

��װAnaconda�󣬻Ὠ��һ������Python��װ����AnacondaĿ¼�����д��Python��������Python.exe����
��Ŀ¼Scripts�д��pip��conda�����ڰ�װά����չ����Lib/site-packages�д���˰�װ����չ����
��IPython��Jupyter�ȣ�����ͨ������鿴��װ����Щ��չ����

### (3) ����

(1) �����д�������<br>
�����װ��������·������������ֱ������:<br>
`\> python` <br>
�����װ��û������·����������������Ҫ����Anaconda��װĿ¼��scripts��Ŀ¼:<br>
`scripts > python`

(2) Windows�˵�<br>
��Windows�˵��У��ҵ�Anaconda�����й����

(3) [Anaconda Powershell Prompt] Powershell�����й���<br>
�ù����ṩ���������д��ڵ�Python�����������п���ʹ������Linux��Ŀ¼�ļ����

(4) [Anaconda Prompt] Prompt�����й���<br>
�ù��߿����ṩ����Windows�����д��ڵ�Python�������ڸô�����ʹ��Dos���

(5) [Jupyter Notebook] Jupyter��������<br>
������������еļ��ɿ����������Ե�ԪΪ��λ�������нű���Notebook���к�
�����һ�������д������е�ϵͳ״̬��ͬʱ�����������������̽��档

(6)Spyder] ���ɿ�������<br>
Spyder��һ����IDLE��רҵ���Ĵ���༭�������ߣ������ص����ṩ�˾�������Matlab�ġ������ռ䡱��
���п��Է���ع۲��޸�����ֵ���ڴ������÷��棬Spyder��Ϯ�˴��������༭���ķ��
�ɴ��봰�ڡ������ռ䴰�ڡ�����̨���ڹ��ɣ����Ը����Լ���ϲ�õ������ǵ�λ�úʹ�С��
ͨ���ڱ༭�������ÿ��Ʒ���SpyderҲʵ�������Ƶĵ�Ԫʽ�ű�����

## 2. [Anaconda Navigator] ����̨<br>
��Windows�˵��У��ҵ�Anaconda�����й�Anaconda Navigator���

## 3. ʹ��conda�������л���

conda��Anaconda���õĻ��������ߣ����зḻ�Ĺ����ܣ������鿴�����ء�����Python���������ȡ�

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
