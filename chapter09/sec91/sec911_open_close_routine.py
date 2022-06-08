# coding = utf8


def demo_for_in_file(filename):
    f = open(filename, 'r', encoding='utf8')
    for line in f:
        print(line.encode())	        # 处理读出的行
    f.close()		                    # 最后关闭文件十分重要，完成读写后文件不关闭会导致很多问题


def demo2_try_except_file(filename):
    f = None
    try:
        f = open(filename, 'r+', encoding='utf8')
        for line in f:
            print(line)
    except FileNotFoundError as e:		# 截获异常
        print(e)			            # 打印错误信息
    except IOError as e:		        # 多次截获异常
        print(e)
    finally:			# 执行关闭文件操作
        if f:           # 如果不设置检测，会再次触发异常
            f.close()


def demo3_with_file(filename):
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            print(line, end='')		# 不打印最后的字符'\n'


if __name__ == '__main__':
    demo_for_in_file('temp_newline.txt')
    demo2_try_except_file('temp_newline3.txt')
    demo3_with_file('temp_newline.txt')
