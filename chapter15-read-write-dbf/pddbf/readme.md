pddbf
=======

Functions
---------
实现dbf文件数据到pandas.DataFrame的转换

目前支持的dbf文件版本及字段格式：
- Visual Foxpro 3-9，dBase III文件
- C, N, D, B

从dbf文件读取数据：
- 不能解析的数据转换为object

将DataFrame数据写为dbf文件数据
- 不能转换格式的数据转换为字符串，写为C格式

Requirements
-------------

* Python -- one of the following:

    - CPython_ : 3.5 and newer
    - PyPy_ : Latest 3.x version


CPython: https://www.python.org/

PyPy: https://pypy.org/


Installation
------------

Package is uploaded on `PyPI <https://pypi.org/project/py2dbf>`_.

You can install it with pip::

    $ python3 -m pip install pddbf

    > pip install pddbf



Documentation
-------------

Documentation is available online: https://pymysql.readthedocs.io/

For support, please refer to the `StackOverflow
<https://stackoverflow.com/questions/tagged/pymysql>`_.


Example
-------

The following examples make use of a simple table

.. code:: sql

CREATE TABLE `users` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`email` varchar(255) COLLATE utf8_bin NOT NULL,
`password` varchar(255) COLLATE utf8_bin NOT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
AUTO_INCREMENT=1 ;


.. code:: python

    import pymysql.cursors

    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='user',
                                 password='passwd',
                                 database='db',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ('webmaster@python.org',))
            result = cursor.fetchone()
            print(result)


This example will print:

.. code:: python

    {'password': 'very-secret', 'id': 1}


Resources
---------

* DB-API 2.0: https://www.python.org/dev/peps/pep-0249/

* MySQL Reference Manuals: https://dev.mysql.com/doc/

* MySQL client/server protocol:
  https://dev.mysql.com/doc/internals/en/client-server-protocol.html

* "Connector" channel in MySQL Community Slack:
  https://lefred.be/mysql-community-on-slack/

* PyMySQL mailing list: https://groups.google.com/forum/#!forum/pymysql-users

License
-------

PyMySQL is released under the MIT License. See LICENSE for more information.