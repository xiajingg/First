#连接数据库
import mysql.connector

conn = mysql.connector.connect(host='0.tcp.ngrok.io', port=12181, user='root', password='xj663812', database='demo')
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
