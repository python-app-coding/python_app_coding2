Temperature Conversion between Fahrenheit and Celsius
=====================================================

1. Foo
----------
Foo 是个示例第三方库，演示Python项目的基本目录结构及组成文件

2. 下载安装
----------

可以使用pip安装第三方库Foo: ::

 > pip install foo_pkg_author

3. 调用方式
----------
导入方式:

>>> import foo
>>> foo.hell()

直接运行::

 > hello

4. 项目结构
---------------
Foo包含下面的目录和文件 ::

  foo
  |-- LICENSE
  |-- README.rst
  |-- pyproject.toml
  |-- src
       |-- foo
           |-- __init__.py
           |-- hello.py
       |-- tests
           |-- test_hello.py
  |-- docs/
       |-- index.rst

5. FAQ
-------
1) 从哪里下载foo_pkg_author ?

   foo_pkg_author已经上传PyPI，可以使用pip install直接安装.

2) 如何导入foo ?

>>> import foo_pkg

3) 如何调用foo_pkg的模块 ?

   foo_pkg只有模块hello, 使用下面的方式导入 :

   >>> import foo_pkg.hello as hello

   然后调用模块hello的方法hello: ::

   python code:

   >>> hello.hello()
   Hello, World!

