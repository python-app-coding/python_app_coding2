# coding = utf8

import os
import tempfile
import time

tfname = tempfile.mkstemp(prefix="temp_", dir='.')
os.close(tfname[0])
print("file: ", tfname[1])
ftime = os.path.getatime(tfname[1])
print("os.path.getatime: ", time.localtime(ftime))

tdname = tempfile.mkdtemp(prefix="temp_", dir='.')
print("temp path: ", tdname)
mtime = time.localtime(os.path.getmtime(tdname))
print("modi time: ", mtime)		        # 获取目录test的最近修改时间
fsize = os.path.getsize(tfname[1])		        # 获取文件大小（字节数）
print("file size: ", fsize)
# 1165
dsize = os.path.getsize(tdname)		            # 目录大小返回0
print("path size: ", fsize)

# 删除临时文件
os.remove(tfname[1])
