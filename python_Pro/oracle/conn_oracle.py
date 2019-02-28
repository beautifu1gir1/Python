import cx_Oracle as cx

#连接Oracle    必须是11.2以上的版本
conn = cx.connect("student/student@127.0.0.1/XE")
print(conn)

cxcursor = conn.cursor()

sql="select * from t_student"

cxcursor.execute(sql)

datas = cxcursor.fetchall()
print(datas)