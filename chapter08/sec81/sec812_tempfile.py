# coding = utf8

import tempfile as tpf
import os

# 只能保证在生成文件名的时间点没有重名冲突
r0 = tpf.mktemp(suffix='0', prefix='temp_', dir='.')
print("created temp file: ", r0)
print(os.path.isfile(r0))
# False

# 调用mkstemp创建空文件
r1 = tpf.mkstemp(prefix='temp_', suffix='1', dir='.', text=True)	# 以文本方式打开文件
print("created temp file: ", r1)
# (6, 'E:\\Project_skillful_python\\0refmi8ow1')		# 返回打开文件的句柄6，以及文件名
os.close(r1[0])					# 关闭文件

# 调用mkdtemp创建临时目录
r2 = tpf.mkdtemp(prefix='temp_', suffix='bb', dir='.')	# 创建当前目录的临时子目录
print("created temp path: ", r2)
# '.\\a_3bzis68c_b'			# 返回创建的相对路径目录名

if input("delete created files and dir?(y/n)") in ['y', 'Y']:
    os.remove(r1[1])
    os.rmdir(r2)
    print(f"have removed: \n{r1[1]}, \n{r2}")

# 使用TemptoryFile创建临时文件
with tpf.TemporaryFile() as fp:		        # 创建临时文件，命名文件描述符为fp
    fp.write(b'Hello world!')		        # 向文件中写入二进制数据
    fp.seek(0)			                    # 将读写文件指针指向开始处
    print(fp.read())			            # 读出文件所有内容
# b'Hello world!'				            # 运行结果是读出内容。with语句自动关闭删除文件

# 使用temptoryDirectory创建临时目录
dname = []
with tpf.TemporaryDirectory() as tmpdirname:		# 创建临时目录
    print('temporary directory', tmpdirname)		# 输出目录名（在系统指定目录中）
    dname.append(tmpdirname)
    print(os.path.isdir(dname[0]))
    # True
print(os.path.isdir(dname[0]))
# False					# 目录已经删除
