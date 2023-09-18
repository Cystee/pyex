cha="〇一二三四五六七八九"
toR="0123456789"
s=input("输入一个数字：")
for i in range(10):
    s=s.replace(toR[i],cha[i])
print(s)
