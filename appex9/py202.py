data=input()
ls1=data.split()
d={}
for i in range(len(ls1)):
    d[ls1[i]]=d.get(ls1[i],0)+1
ls2=list(d.items())
ls2.sort(key=lambda x:x[1],reverse=True)
print(ls2)
