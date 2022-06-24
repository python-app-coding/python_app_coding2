# coding = utf8


import pandas as pd
import sqlite3
import sqlalchemy

def make_sqlite_table():
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()

    # 如果表存在先删除
    cur.execute('''DROP TABLE IF EXISTS test_table''')

    # 在数据库中创建表
    create_sql = '''CREATE TABLE IF NOT EXISTS test_table(id text, name text, math integer, art real)'''
    cur.execute(create_sql)

    #  使用参数填充方式插入多条记录
    some_students = [('21102', 'Liu', 100, 45),
                     ('21103', 'Ma', 100, 72),
                     ('21104', 'Si', 50, 53)]
    cur.executemany('INSERT INTO test_table VALUES (?,?,?,?)', some_students)
    conn.commit()

    # 使用参数替换方式
    s = (0,)
    select_str = 'SELECT * FROM test_table WHERE art >= ?'
    cur.execute(select_str, s)
    print("\n--- read by cursor.execute('{}', {}) ---".format(select_str, s))
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def demo_read_sql():
    # tests table read
    # print("\n--- read by cursor.execute(sql) ---")
    # conn = sqlite3.connect('students.db')
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM test_table")
    # rs = cursor.fetchall()
    # for r in rs: print(r)
    # conn.close()

    conn = sqlite3.connect('students.db')
    print("\n--- read by pandas.read_sql with sqlite3.connect---")
    sqlstr = "select * from test_table where art >= %2d"
    val = 0
    df = pd.read_sql(sql=sqlstr % val, con=conn)
    print(df)
    conn.close()

    engine =sqlalchemy.create_engine('sqlite+pysqlite:///students.db')
    print("\n--- read by pandas.read_sql ---")
    sqlstr = "select * from test_table where art >= %2d"
    val = 0
    df = pd.read_sql(sql=sqlstr % val, con=engine)
    print(df)
    df2 = pd.read_sql("test_table", con=engine)
    print(df2)


def demo2_read_sql_query():
    print("\n--- read by pandas.read_query ---")
    engine = sqlalchemy.create_engine('sqlite+pysqlite:///students.db')
    # conn = engine.connect()
    df = pd.read_sql_query(sql="select * from test_table", con=engine)
    # conn.close()
    print(df)

def demo3_read_sql_table():
    print("\n--- read by pandas.read_sql_table ---")
    engine = sqlalchemy.create_engine('sqlite+pysqlite:///students.db')
    conn = engine.connect()
    df = pd.read_sql_table("test_table", con=conn)
    print(df)

    # TypeError: 不能使用sql语句
    # df2 = pd.read_sql_table(sql="select * from test_table", con=conn)
    # print(df2)

    conn.close()


if __name__ == "__main__":
    # make_sqlite_table()
    demo_read_sql()
    demo2_read_sql_query()
    demo3_read_sql_table()
