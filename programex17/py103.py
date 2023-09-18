import random
random.seed(0)
r=0
for i in range(5):
    r+=pow(random.randint(1,97),2)
print(r)