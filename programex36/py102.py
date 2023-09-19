s=input("输入：")
ls=[]
for i in s[::-1]:
    ls.append(i.upper())
print(",".join(ls))
