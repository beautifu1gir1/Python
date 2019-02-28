# 导入模块，引入类
from pyecharts import Liquid

# 创建水球图对象  （括号内为图名）
liObj=Liquid("人员工资占比图")

#创建的对象内放入数据
liObj.add("人员工资占比",[0.9])

#渲染到一个HTML页面
liObj.render("水球图.html")
