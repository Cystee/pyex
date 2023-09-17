a=[3,6,9]
b=[]
for i in range(3):
    c=eval(input('连续输入三次数字：'))
    b.append(c)
result=0
for i in range(3):
    result+=a[i]*b[i]
print('输出：{}'.format(result))
