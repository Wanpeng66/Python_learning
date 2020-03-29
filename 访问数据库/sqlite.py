# python内置了sqlite数据库
import sqlite3


def CreatAndInsert(conn):
    cursor = conn.cursor()
    cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
    cursor.execute("insert into user (id, name) values ('1', 'Michael')")
    print(cursor.rowcount)
    cursor.close()
    conn.commit()


def search(conn):
    cursor = conn.cursor()
    cursor.execute("select * from user where id=?", (1,))
    all = cursor.fetchall()
    print(all)
    cursor.close()


if __name__ == "__main__":
    conn = sqlite3.connect("C:/Users/14793/Pictures/test.db")
    search(conn)
    conn.close()