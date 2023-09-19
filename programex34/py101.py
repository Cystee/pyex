s=input("输入：")
ttl=0
for c in s[::-1]:
    if c==".":
        break
    ttl+=int(c)
print("{:*>10}".format(ttl))
