ls=input("输入以逗号分隔的三个数字：").split(",")
a,b,c=int(ls[0]),int(ls[1]),int(ls[2])
resultList=[]
for i in range(c):
    resultList.append(a)
    a+=b
print(resultList)

#More Efficiency
a,b,c=eval(input("输入以逗号分隔的三个数字："))
ls=[]
for i in range(c):
    ls.append(a+b*i)
print(ls)