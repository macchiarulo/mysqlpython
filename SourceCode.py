import pymysql

conn = pymysql.connect(host= '[hostname]',user='[log-in]',password='[password]',db='[database name]')

a = conn.cursor()

sql = 'SELECT * from Data'
a.execute(sql)

countrow = a.execute(sql)
print("Number of rows :", countrow)

data = a.fetchone()
print(data)
