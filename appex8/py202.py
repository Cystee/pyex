data=input()
n=0
age=0
num=0
while data:
    n=n+1
    ls=data.split()
    age=age+int(ls[2])
    if ls[1]=="男":
        num+=1
    data=input()
avg=age/n
print("平均年龄：{:.2f} 男性人数：{}".format(avg,num))
