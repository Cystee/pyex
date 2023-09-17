price=160
amount=int(input("购买数量："))
if amount==1:
    print("总额为：160")
elif amount>=2 and amount<=4:
    print("总额为：{}".format(amount*160*0.9))
elif amount>=5 and amount<=9:
    print("总额为：{}".format(amount*160*0.8))
else:
    print("总额为：{}".format(amount*160*0.7))