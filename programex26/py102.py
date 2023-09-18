scale=0.0001
def cala(year):
    anum=1*(1+scale)**(365*year*11)
    return anum
ynum=1
while cala(ynum)<100:
    ynum+=1
print("5年后的成就值是{:.0f}".format(cala(5)))
print("{}年后成就值是100".format(ynum))
