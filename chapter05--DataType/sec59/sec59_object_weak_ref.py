# coding: utf8

"""
创建弱引用需要使用weakref模块，weakref.ref可以返回一个对象的弱引用。如果一个变量被赋予弱引用，被引用的对象可以随时被销毁回收，所指向的对象正常存在时，该变量可以正常引用，不存在时则返回None。

 >>> import sys
 >>> import weakref

 >>> class DemoClass2:
 ...     def m1(self):
 ...         return "Demo Class2"

 >>> a = DemoClass2()     		# 创建对象，赋予引用变量a
 >>> a1 = a               		# 增加引用a1
 >>> b = weakref.ref(a)   		# 建立弱引用b
 >>> c = weakref.ref(a)   		# 建立弱引用c
 >>> sys.getrefcount(a)-1
 2

 >>> a.__weakref__, a1.__weakref__      	# 对象属性__weakref中，存储了所建立的弱引用
 (<weakref at 0x000001C1FBEF6638; to 'DemoClass2' at 0x000001C1FBEFF828>,
 <weakref at 0x000001C1FBEF6638; to 'DemoClass2' at 0x000001C1FBEFF828>)

 >>> b, c
 (<weakref at 0x000001C1FBEF6638; to 'DemoClass2' at 0x000001C1FBEFF828>，
 <weakref at 0x000001C1FBEF6638; to 'DemoClass2' at 0x000001C1FBEFF828>)

 >>> id(a), id(a1), id(b), id(c)      	# 各个引用变量的id, 弱引用与引用是不同的变量
(2026480531968, 2026480531968, 2026480536688, 2026480536688)
 >>> a.m1()       		# 使用引用调用对象方法
 'Demo Class2'
 >>> b().m1()     		# 使用弱引用调用对象方法，需要先实例化，使用b()
 'Demo Class2'
 >>> del b      		# 删除弱引用b, 不影响对象的引用计数
 >>> sys.getrefcount(a) - 1
 2
 >>> a = 0
 >>> a1 = 1     		# 赋予a, a1新的引用, 所指向对象DemoClass2()将被回收
 >>> c          		# 然后弱引用失去被引用对象，显示引用无效: dead
 <weakref at 0x000001C1FBEF6638; dead>
 >>> c()        		# 调用无效弱引用，无返回值

"""