from turtle import *
"""
seth(-45)
fd(200)
seth(45)
fd(200)
seth(135)
fd(200)
seth(225)
fd(200)
"""
pensize(2)
h=-45
for i in range(4):
    seth(h+i*90)
    fd(200)
