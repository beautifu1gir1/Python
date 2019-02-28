import pymysql as pm

def queryEmpSalary(* args):
    conn = pm.connect(host="127.0.0.1",port=3306,database="demo",user="root",password="root",charset="utf8")

    dbcursor = conn.cursor()
    sql="SELECT FORMAT(salary/(SELECT SUM(salary) FROM t_students ),2)  FROM t_students WHERE sname=%s"

    dbcursor.execute(sql,args)

    datas = dbcursor.fetchone()

    if datas is None:
        return None
    else:
        #方法返回计算的值
        return datas[0]

'''data = queryEmpSalary("孙婕")
print(data)'''