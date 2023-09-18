a=[3,6,9]
b=eval(input("输入列表："))
'''笨办法
c=[]
for i in range(len(b)):
    c.append(b[i])
    c.append(a[i])
print(c)
'''
j=1
for i in range(len(a)):
    b.insert(j,a[i])
    j+=2
print(b)