from pyecharts import Pie
from liquidView.psours import *

pObj = Pie("男女生占比图")

datas = queryEmpSex()

ats = []
das = []

for value in datas:
    ats.append(value[1])
    das.append(value[0])

pObj.add("男女生占比",ats,das)

pObj.render("p.html")