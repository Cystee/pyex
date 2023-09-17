s=int(input("输入9800到9811之间的一个数字："))

"""笨方法
u_1,u,u__1=chr(s-1),chr(s),chr(s+1)
print("++++{0}{1}{2}++++".format(u_1,u,u__1))
"""

print("{:+^11}".format(chr(s-1)+chr(s)+chr(s+1)))