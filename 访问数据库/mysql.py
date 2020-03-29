# python 连接mysql数据库

import pymysql

if __name__ == "__main__":
    conn = pymysql.connect(user='root', password='123456', database='myshop')
    cursor = conn.cursor()
    cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
    cursor.execute("insert into user (id, name) values (%s, %s)",["1","wp"])
    print(cursor.rowcount)
    cursor.close()
    conn.commit()
    cursor = conn.cursor()
    cursor.execute("select * from user where id = %s",("1",))
    print(cursor.fetchall())
    cursor.close()
    conn.close()