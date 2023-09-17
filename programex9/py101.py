s=input("输入：").split()
x0,y0,x1,y1=eval(s[0]),eval(s[1]),eval(s[2]),eval(s[3])
result=pow((x0-x1)**2+(y0-y1)**2,0.5)
print("{:.2f}".format(result))