import random
seed=eval(input("种子："))
random.seed(seed)
ls=[]
for i in range(26):
    ls.append(chr(ord("a")+i))
for i in range(10):
    ls.append(chr(ord("0")+i))
for i in range(10):
    for j in range(8):
        print(ls[random.randint(0,35)],end="")
    print()
