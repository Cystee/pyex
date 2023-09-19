import random
random.seed(25)
ans=random.randint(1,100)
t=0
while t<6:
    t+=1
    i=int(input("输入："))
    if i<ans:
        print("小了，请再试试")
    elif i>ans:
        print("大了，请再试试")
    else:
        print("恭喜你，猜对了")
        break
else:
    print("谢谢，休息下再试吧")
