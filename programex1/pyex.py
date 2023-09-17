f=open('命运.txt',encoding='UTF-8')
fi=f.read()
for ch in '，。？：！；、…—（）“”《》':
    fi1=fi.replace(ch,'')
d = {}
for i in fi1:
    d[i]=d.get(i,0)+1
l=list(d.items())
l.sort(key=lambda s:s[1],reverse=True)
print("{}:{}".format(l[0][0],l[0][1]))
for n in range(11):
    print(l[n][0],end='')
for ch in ' \n':
    fi2=fi.replace(ch,'')
di={}
for i in fi2:
    di[i]=di.get(i,0)+1
li=list(di.items())
li.sort(key=lambda s:s[1],reverse=True)
import os
os.chdir("./")
os.open("命运-频次排序.txt",os.O_CREAT)
with open("命运-频次排序.txt","w",encoding="utf-8") as fil:
    for m in li:
        fil.write("{}:{},".format(m[0],m[1]))
