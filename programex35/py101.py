ls=eval(input("输入："))
s=""
for i in ls:
    if type(i)==type(""):
        s+=i
print(s)
