f=open("命运.txt",encoding="utf-8").read()
d = {}
for cha in "\n":
    f=f.replace(cha,"")
for i in f:
    d[i]=d.get(i,0)+1
ls = list(d.items())
ls.sort(key=lambda x:x[1], reverse=True)
for i in range(11):
    print(ls[i][0],end="")