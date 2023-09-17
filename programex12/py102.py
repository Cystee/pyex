a,b=0,1
'''笨方法
c=1
ls=[a,b]
while c<=100:
    ls.append(c)
    a,b=b,a+b
    c=a+b
for i in ls:
    print(i,end=' ')
'''
while a<=100:
    print(a,end=',')
    a,b=b,a+b
