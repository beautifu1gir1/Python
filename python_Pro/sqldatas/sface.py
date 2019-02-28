import pymysql as pm

# 连接数据库的方法
def connDB1():
    conn = pm.connect(host="127.0.0.1", port=3306, database="demo", user="root", password="root", charset="utf8")
    return conn

def connDB():
    conn = pm.connect(host="127.0.0.1", port=3306, database="njpi", user="root", password="root", charset="utf8")
    return conn

#查询头像路径
def queryFacePath(* args):
    #conn = pm.connect(host="127.0.0.1",port=3306,database="demo",user="root",password="root",charset="utf8")

    conn = connDB1()

    dbcursor = conn.cursor()

    sql="SELECT sface FROM t_students WHERE sname=%s"

    dbcursor.execute(sql,args)

    datas = dbcursor.fetchone()

    print(datas)

    return datas[0]

#查询指定用户的
def queryinfor(* args):
    #conn = pm.connect(host="127.0.0.1",port=3306,database="demo",user="root",password="root",charset="utf8")

    conn = connDB1()
    dbcursor = conn.cursor()

    sql = "SELECT  sphone,sface,saddress,ssex,mimage,audio,video FROM t_students WHERE  sname =%s"

    dbcursor.execute(sql, args)

    datas = dbcursor.fetchone()
    if datas is None:
        data = ("无","/usering/no.jpg","？","母鸡","无","无","无")
        return data
    else:
        return datas

def queryDBAll():

    conn = connDB()
    dbcoursor = conn.cursor()

    sql="SELECT sname,sphone,sqq,sphoto  FROM t_students WHERE scid='软件技术'"

    dbcoursor.execute(sql)

    datas = dbcoursor.fetchall()

    print(datas)
    return datas
#queryDBAll()
def checkDBUser(* args):

    conn = connDB()

    dbcursor = conn.cursor()
    sql = "SELECT COUNT(*) FROM t_students WHERE sname = %s"

    dbcursor.execute(sql,args)

    data = dbcursor.fetchone()

    # print(data)
    # print(data[0])
    return data[0]
