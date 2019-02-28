from pyecharts import Liquid

from liquidView.sours import *

name =input("请输入姓名：")

data = queryEmpSalary(name)

# print("----------",data)

if data is None:
    print("用户不存在")
else:
    lidata = []
    lidata.append(data)
    print(lidata)

    liObj = Liquid("员工工资占比图")

    liObj.add("员工工资占比", lidata)

    liObj.render(name + ".html")
