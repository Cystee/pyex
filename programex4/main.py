import jieba
s=input("输入：（吃葡萄不吐葡萄皮）")
ls=jieba.lcut(s)
num=0
for i in ls:
    num+=len(i)
result=num/len(ls)
print("输出：{:.1f}".format(result))