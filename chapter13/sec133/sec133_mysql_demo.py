# coding = utf8

import pymysql


def demo1_conn_mysql():
    """
    使用pymysql连接读取MySql数据库数据
    """
    # 建立于MySql的连接
    conn = pymysql.connect(
            host='127.0.0.1',
            user='test',
            passwd='test',
            db='students',
            port=3306,
            charset='utf8'
    )
    # 创建游标对象
    cursor = conn.cursor()
    # 执行查询
    cursor.execute("""select * from score""")
    # 获取查询结果
    records = cursor.fetchmany(3)
    for row in records: print(row)
    # (('211001', 'MengBoli', 120, 56.2), ('211002', 'DengTong', 110, 86.7))


if __name__ == "__main__":
    demo1_conn_mysql()
