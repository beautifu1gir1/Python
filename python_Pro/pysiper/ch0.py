#爬虫的第一个框架 pyquery，使用css选择器的语法进行爬取
#只要把链接或者说是html构造成pyquery对象，就可以使用里面的内置方法

from pyquery import PyQuery
from pysiper.db import *

#定向爬取的url="http://ent.163.com/movie/"
url= "https://blog.csdn.net/kongxx"

#构建整个的url的PyQuery
doc = PyQuery(url)
#打印输出
#print(doc)

#爬取到本地文件，方便分析
'''with open("a1.txt","w",encoding="UTF-8") as fw:
    fw.write(doc.html())'''

#找节点，爬取数据
lists = doc(".article-list  .article-item-box ")
print(lists.size())

for item in lists:
    divobj = PyQuery(item)
    #print(divobj)
    title= divobj("h4 a")
    #print(title.text())
    con = divobj("p a")
    print(con.attr("href"))
    #print("-->",con.text())
    info = divobj("div p  span")
    date=info(".date")
    read = info(".read-num")
    #print(read.text())
    #adddata(title.text(),str(con.attr("href")),con.text(),read.text(),date.text())
    #print("数据入库成功")
