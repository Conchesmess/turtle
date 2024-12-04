from turtle import *

speed(13)
colormode(255)
WIDTH, HEIGHT = 1000, 800
screen = Screen()
screen.setup(WIDTH, HEIGHT)


def sunset():
    penup()
    x=-500
    y=400
    r=255
    g=255
    b=0
    for i in range(400):
        pencolor(r,int(g),b)
        goto(x,y)
        pendown()
        setheading(0)
        fd(window_width())
        bk(window_width())
        y=y-1
        g=g-0.5
        if g<0:
            g=0

sunset()

done()