s1 = "123"
print(s1)
print(type(s1))
print(id(s1))

print("-----------")
s2 = "123"
print(s2)
print(type(s2))
print(id(s2))

print("-----------")
print(s1 == s2)
print(s1 is s2)

print("-----------")
s3= s1+s2
print(s3)
print(type(s3))     #type为 str

print("---------")
s4 =s1,s2
print(s4)
print(type(s4))     #type为 tuple(元祖)

print("----------")
s5="12"
s5=s5+"3"
print(s5)
print(type(s5))
print(s5 ==s2)      #值是相同的
print(s5 is s2)     #id不相同（例：同名但是不同的人）