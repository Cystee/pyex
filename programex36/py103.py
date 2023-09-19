import random
random.seed(100)
n=int(input("输入："))
ls=[]
for i in range(10):
    ls.append(str(random.randint(1,n)))
print(",".join(ls))
