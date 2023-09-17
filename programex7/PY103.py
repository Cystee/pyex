import jieba
s=input("输入：")
ls=jieba.lcut(s)
ls1=ls[::-1]
for i in ls1:
    print(i,end="")