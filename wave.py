from turtle import *

def wave(size):
    bgcolor("blue")
    colormode(255)
    pencolor(0,0,100)
    pensize(10)
    penup()
    x = -500
    y = 0
    for j in range(4):
        penup()
        goto(x,y)
        pendown()
        for i in range(10):
            setheading(315)
            circle(size,90)
        y = y - 40

wave(60)

done()