while True:
    try:
        n=eval(input("请输入一个正整数："))
        if n>0 and n%1==0:
            print(n)
            break
        else:
            print("请输入正整数！")
    except:
        print("请输入正整数！")
