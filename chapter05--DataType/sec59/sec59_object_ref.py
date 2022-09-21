# coding: utf8

"""
整数是不可修改类型：
>>> a = 500			# 整数是不可修改的对象类型
>>> b = a
>>> print(id(a) == id(b))	    # 两个变量指向的对象是相同的
True
>>> a = 6
>>> id(a) == id(b)			# 改变值后，a已经指向了新的对象, id值不再相同
False

字符串为不可修改类型：
>>> s = '123'			# 字符串不可修改类型
>>> id_s1 = id(s)

# >>> s[0] = 'a'			# 试图修改字符串，会触发异常
#  .....
# TypeError: 'str' object does not support item assignment

>>> s = 'a23'			# 使用重新赋值方式，s已经不是原来的对象
>>> id(s) != id_s1
True

列表为可修改类型：
>>> c = [1,2,3]			# c是一个列表，列表是可修改对象
>>> id_c = id(c)
>>> c[0] = 100			# 改变c的值
>>> id(c) == id(c)			# id没有改变
True


对象引用示例：
 >>> class DemoClass1:		# 定义一个普通类
 ...     pass

 >>> a = DemoClass1()              	# 建立对DemoClass1()的引用a
 >>> b = a                         	# 增加对DemoClass1()的引用b
 >>> c = [a, b, DemoClass1()]      	# 列表元素建立了自己的引用，新建对象DemoClass1()是新的引用
 >>> import sys
 >>> sys.getrefcount(a)-1		    # 获取a指向对象的引用计数，去掉获取函数临时的引用
 4

 >>> id(a) == id(c[2])		        # 通过查看两个对象的标识看到, c[2]与a指向了不同的对象
 False

 >>> del b                     	    # 删除引用b
 >>> sys.getrefcount(a)-1        	# 剩下3个引用：a, c[0], c[1]
 3
 >>> del c[2]                  	    # 删除c[2]，不影响a指向对象的引用
 >>> sys.getrefcount(a)-1
 3


 在使用容器类对象时，需要将其元素与容器对象本身相区别。
 >>> a = [1, 2, 3, 4, 5]                   	# 创建容器对象并建立引用a， 每个元素引用各自的对象
 >>> b = a                                 	# 变量b引用了a指向的列表
 >>> sys.getrefcount(a)-1                  	# 列表对象的引用计数
 2
 >>> sys.getrefcount(a[0])-1 > 10           # 列表元素指向对象的引用计数（整数1的引用计数）
 True
 >>> [sys.getrefcount(x)-1>10 for x in a]   # 查看各个列表元素所指向对象的引用计数, 注意，迭代过程中增加了一个临时引用
 [True, True, True, True, True]


 小整数对象不会被回收，它们的引用会很多。而不在[-5, 256]内的整数，被视为非常用整数对象，每次引用时都会创建新对象。
 >>> a = -5                              # 创建小整数对象
 >>> sys.getrefcount(a)-1 > 1            # 显示整数-5的引用, 引用计数较多，包括系统内很多使用-5的变量引用
 True
 >>> x =100; y = 100	                # 引用小整数池中的对象
 >>> id(x) == id(y)	                    # x和y的标签相同，指向同一个对象
 True
 >>> x1 = 1000; y1 = 1000	            # 引用小整数池之外的整数
 >>> id(x1) == id(y1)	                # x1和y1的标签不相同，指向不同的对象(有时也会分配相同地址！)
 True


 对象交叉循环引用示例：
1）定义一个类，带有对象变量x，定义对象销毁时的方法__del__,在其中显示销毁对象的有关信息，用于观察本对象是否被回收：
>>> class DemoClass3:
...    def __init__(self, x):
...        self.x = x
...
...    def __del__(self):
...        print('{} is collected!'.format(self.x))


2）由上面的类创建两个对象，通过对像属性x赋值为相互引用
>>> obj1 = DemoClass3(100)
>>> obj2 = DemoClass3(200)
>>> obj1.x = obj2
>>> obj2.x = obj1

3）删除两个相互引用的对象，系统并没有马上销毁回收，因为没有执行__del__方法：
>>> id1 = hex(id(obj1)).upper()
>>> id1
'0X15B501FCA30'
>>> id2 = hex(id(obj2)).upper()
>>> id2
'0X15B501FCBB0'

>>> del obj1
>>> del obj2
>>> import gc
>>> tracked = gc.get_objects()

# 查找内存中的对象，发现obj1仍然没有删除回收!
# >>> [ob for ob in tracked if id1[2:] in str(ob) or id2[2:] in str(ob)]
# [... object at 0x0000015B501FCA30>,
# ... object at 0x0000015B501FCBB0>,
# ...]

4）使用gc模块的collect方法强制回收，看到__del__方法已经执行
# >>> gc.collect()
# <...<locals>.DemoClass3 object at 0x0000015B501FCA30> is collected!
# <...<locals>.DemoClass3 object at 0x0000015B501FCBB0> is collected!
"""