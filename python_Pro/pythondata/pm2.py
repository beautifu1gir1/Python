import  pymysql as pm

conn = pm.connect(host="127.0.0.1",port=3306,database="demo",user="root",password="root",charset="utf8")
print(conn)

dbcursor = conn.cursor()

sql="INSERT INTO t_students(sname,spwd,sphone,sface,saddress,ssex)VALUES(%s,%s,%s,%s,%s,%s)"
dbcursor.execute(sql,("陈大炮","123456","18751810007","a7.jpg","河南","女"))

conn.commit()