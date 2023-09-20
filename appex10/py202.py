data=input()
d={}
n=0
while data:
    l=data.split()
    d[l[0]]=l[1]
    n+=1
    data=input()
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
print(ls[0][0],ls[0][1])
ls.sort(key=lambda x:x[1])
print(ls[0][0],ls[0][1])
avg=0
m=0
for i in d.values():
    avg+=int(i)
    m+=1
avg=avg/m
print("{:.2f}".format(avg))
