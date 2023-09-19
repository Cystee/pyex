import time
n=float(input("输入："))
ls=time.ctime(n).split(" ")
print(ls)
print(ls[3][0:2])
