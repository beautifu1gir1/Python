import  pymysql as pm

def addEmp(* args):
    conn=pm.connect(host="127.0.0.1",port=3306,database="demo",user="root",password="root",charset="utf8")

    dbcursor=conn.cursor()

    sql="UPDATE t_students SET spwd=%s WHERE sid=%s"

    dbcursor.execute(sql,args)

    conn.commit()

addEmp("123456","2")