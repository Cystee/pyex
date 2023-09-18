a,b,c=eval(input("输入三个数字："))
ls=[]
for i in range(c):
    ls.append(str(a))
    a*=b
print(",".join(ls))
