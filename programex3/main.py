f=open("命运.txt",encoding="utf-8").read()
for cha in " \n":
    f=f.replace(cha,"")
d = {}
for i in f:
    d[i]=d.get(i,0)+1
ls = list(d.items())
ls.sort(key=lambda x:x[1], reverse=True)
f=open("命运-频次排序.txt","w",encoding="utf-8")
for i in ls:
    f.write("{}:{},".format(i[0],i[1]))
