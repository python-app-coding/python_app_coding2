Foo
=========

1. Introduction 简介
-------------------

Foo is a demo project for creating and distributing python lib:

- it provides a directories to make a project.

- a demo project that available to upload to pypi.org

Foo 是一个演示项目，用于展示创建和分发Python第三方库:

- 提供了一个Python第三方库项目目录文件样板

- 打包后可以上传到pypi.org


[ContactProjectAuthor](https://gitee.com/applied/python_app_coding)

[联系](applied_python@163.com)


2. Installation / 安装
--------------------------

::

    pip install foo_pkg_author



3. Usage / 使用
--------------------------


import mode / 导入方式 :

::

    >>> from foo_pkg import hello
    >>> hello.hello()
    Hello, World!

run mode / 运行方式：

::

    > hello
    Hello, World!

4. Project 项目结构
------------------
Foo structure ::

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

5. FAQ 常见问题
--------------
1) Where to download foo_pkg_author ?

   foo_pkg_author is on PyPI，please use pip to install.

2) How to import foo ?

>>> import foo_pkg

3) How to call module in foo_pkg ?

   hello is an only module of foo_pkg, import it as follow:

   >>> import foo_pkg.hello as hello

   then call method hello: ::

   python code:

   >>> hello.hello()
   Hello, World!

.. *ref*: ..\docs\index.rst
