from turtle import *

X_len=400
Y_len=300
x0=-200
y0=-100

penup()
goto(x0,y0)
pendown()

left(90)
fd(Y_len)
goto(x0,y0)
right(90)
fd(X_len)
goto(x0,y0)

Ls=[69,292,33,131,61,254]

color("red")
pensize(5)

for i in range(len(Ls)):
    penup()
    goto(x0+(i+1)*50,y0)
    seth(90)
    pendown()
    fd(Ls[i])

done()
