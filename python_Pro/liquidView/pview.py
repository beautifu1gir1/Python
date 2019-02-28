# 引入饼图类
from pyecharts import Pie

# 创建一个饼图对象
pieObj = Pie("占比饼图")

#添加数据
#方法一：pieObj.add("男女生占比",["男","女"],[5,3])
#方法二：
#属性
attrs=["男","女"]
#数据
datas=[5,3]

pieObj.add("男女生占比",attrs,datas)

#渲染到一个HTML页面
pieObj.render("饼图.html")

