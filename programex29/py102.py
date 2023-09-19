s=input('输入：')
dnum,dalp=0,0
for i in s:
    if i.isnumeric():
        dnum+=1
    elif i. isalpha():
        dalp+=1
    else:
        pass
print('字母个数{0}，数字个数{1}'.format(dalp,dnum))
