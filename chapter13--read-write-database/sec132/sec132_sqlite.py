# coding = utf8

import sqlite3
import faker

def demo1_create_sqlite_table():
    # Sqlite数据库访问示例：
    # （1）创建数据库并写入数据
    # 建立连接，获取连接对象
    conn = sqlite3.connect('students.db')

    # 创建游标对象
    cursor = conn.cursor()

    # 如果存在表，先删除
    cursor.execute('''DROP TABLE IF EXISTS score''')

    # 在数据库中创建表
    create_sql = '''CREATE TABLE IF NOT EXISTS score(id text, name text, math integer, art real)'''
    cursor.execute(create_sql)

    # 插入一行数据
    insert_sql1 = "INSERT INTO score VALUES ('21101','John Hann', 90, 80.5)"
    cursor.execute(insert_sql1)
    # 使用参数形式
    insert_sql2 = "INSERT INTO score VALUES (?, ?, ?, ?);"
    cursor.execute(insert_sql2, ('21101','John Smith', 67, 50.5))

    # 插入多行数据
    insert_num = 3
    fk = faker.Faker('zh_cn')
    values = [(str(21101+i), fk.name(), fk.random.randint(60,100), fk.random.randint(50, 90))
              for i in range(insert_num)]
    insert_sql = '''INSERT INTO score (id, name, math, art) VALUES(?, ?, ?, ?)'''
    cursor.executemany(insert_sql, values)

    # 提交事务，永久保存数据到数据库
    conn.commit()

    # 关闭连接。在关闭前，一定注意是否需要提交事务，否则数据修改会无效。
    cursor.close()
    conn.close()


def demo2_read_sqlite_table():
    # （2）读取数据库数据
    # 连接数据库、创建游标对象
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # 从数据库表中读取数据
    cursor.execute('''SELECT * from score''')
    print("\n--- read all ---")
    r1 = cursor.fetchall()
    for col in r1:
        print(col)

    # 使用fetch再获取数据，需要设置执行查询
    cursor.execute('''SELECT * from score''')
    print("\n--- read 5 rows ---")
    r2 = cursor.fetchmany(5)
    for col in r2:
        print(col)

    cursor.close()
    conn.close()


def demo3_sql_by_placeholder():
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()

    #  使用安全方式插入多条记录：
    some_students = [('21102', 'Liu', 100, 45),
             	     ('21103', 'Ma', 100, 72),
	        	     ('21104', 'Si', 50, 53)]
    cur.executemany('INSERT INTO score VALUES (?,?,?,?)', some_students)
    conn.commit()

    # 不使用占位符的非安全性方式：
    print("\n--- select art >= 70")
    cur.execute("SELECT * FROM score WHERE art >= 70")
    for row in cur.fetchall(): print(row)

    # 使用参数替换的安全方式：
    s = (70,)
    cur.execute('SELECT * FROM score WHERE art >= ?', s)
    print("\n--- select art >= ?, 70")
    for row in cur.fetchall(): print(row)

    conn.close()


def demo4_sql_master():
    """
    sqlite_master表结构定义：
    type TEXT			    # 数据对象类型
    name TEXT			    # 数据对象名称
    tbl_name TEXT		    # 表或视图名称
    rootpage INTEGER	    # 根页号(表或索引在B-树根页中的页号)
    sql TEXT		        # SQL语句（创建该对象的Create语句）
    """
    # 连接数据库
    cnn = sqlite3.connect("students.db")
    cur = cnn.cursor()

    # 查看数据库中存储数据的信息
    cur.execute("""select * from sqlite_master""")
    info = cur.fetchall()
    for row in info: print(row)

    # 查看数据库中存储数据表
    cur.execute("""select * from sqlite_master where type = ?""", ("table",))
    info_tables = cur.fetchall()
    for row in info_tables: print(row)

    cur.close()
    cnn.close()


if __name__ == "__main__":
    # demo1_create_sqlite_table()
    # demo2_read_sqlite_table()
    # demo3_sql_by_placeholder()
    demo4_sql_master()
