from turtle import *
colormode(255)
speed(13)

def sun(size):
    r=255
    g=255
    b=0
    loops = size
    for i in range(loops):
        pencolor(r,g,b)
        dot(size)
        size=size-1
        g=g-1
        if g<0:
            g=0

sun(300)

done()