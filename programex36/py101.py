n=int(input("输入："))
x=0
for i in range(1,n):
    x+=1
    for t in range(x,n):
        print(t,end=" ")
    print()
