"""
数据库的操作

conn.commit()
"""

import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='rootXKY123',
    database='xky_course',
    charset='utf8',
    autocommit=False
)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'select * from course'
res = cursor.execute(sql)

print(res)
print(cursor.fetchone())
print(cursor.fetchall())
# conn.commit()  对修改二次确认
