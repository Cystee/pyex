n=int(input("输入："))
if n%2!=0:
    re=0
    for i in range(1,n+1,2):
        re+=1/i
    print("{:.2f}".format(re))
if n%2==0:
    res=0
    for i in range(2,n+1,2):
        res+=1/i
    print("{:.2f}".format(res))
