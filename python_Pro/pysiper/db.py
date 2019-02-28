import pymysql

def   adddata(*args):
    print(args)
    conn=pymysql.connect(host="127.0.0.1",port=3306,database="BLOG",user="root",
                         password="root",charset="utf8")
    print(conn)

    sql="insert  into   articles(user_id,article_title,article_url,article_content,article_views,article_date) " \
        " values(1,%s,%s,%s,%s,%s)"

    dbcursor=conn.cursor()
    dbcursor.execute(sql,args)
    #记着一定要提交
    conn.commit()





