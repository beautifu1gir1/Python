#python 列表  []
#列表是不定长不定值
a1=[1,2,3,4]
print(a1)
print(type(a1))
print(id(a1))

print("-----------")
a2=[1,2,3,4]
print(a1==a2)
print(a1 is a2)

print("----------")
#添加元素
a1.append(5)
print(a1)

a1[0]=7
print(a1)
print("-----------")

#字典类型  {dict}           d = {key1 : value1, key2 : value2 }
maps ={"name":"小仙女","age":"18"}
print(maps)
print(type(maps))
print(maps["name"])

# set 类型   有键，但是没有对应的值，切不能 重复
set1={"1","2","1"}
print(set1)