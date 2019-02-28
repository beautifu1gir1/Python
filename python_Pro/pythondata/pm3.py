import  pymysql

#    创建一个addEmp方法
# def addEmp(* args):  * args 可变参数    方法的参数是一个元祖（）      调用时，不要带*
def addEmp(name,pwd,phone,face,address,sex):
    conn = pymysql.connect(host="127.0.0.1",port=3306,database="demo",user="root",password="root",charset="utf8")

    dbcursor = conn.cursor()

    sql = "INSERT INTO t_students(sname,spwd,sphone,sface,saddress,ssex)" \
          "VALUES(%s,%s,%s,%s,%s,%s);"

    dbcursor.execute(sql,(name,pwd,phone,face,address,sex))

    conn.commit()
    print("插入成功")

# 调用创建的方法
#addEmp("高雪婷","123456","1875181008","a8.jpg","徐州","女")
def addDB(* args):
    conn = pymysql.connect(host="127.0.0.1", port=3306, database="demo", user="root", password="root", charset="utf8")

    dbcursor = conn.cursor()

    sql = "INSERT INTO t_students(sname,spwd,sphone,sface,saddress,ssex)" \
          "VALUES(%s,%s,%s,%s,%s,%s);"

    datas= dbcursor.execute(sql, args)

    conn.commit()
    print(datas)
    print("插入成功")
addDB("高雪婷","123456","1875181008",a8.jpg,"徐州","女")