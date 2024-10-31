from turtle import *
#rgb(165, 42, 42)
#rgb(218, 160, 109)
size = 40
r = 165
g = 42
b = 42
colormode(255)

for i in range(20):
    pensize(size)
    pencolor(r,g,b)
    goto(0, 200)
    goto(0,0)
    size=size-2
    r = r + 5
    if r >218:
        r = 218
    g = g + 5
    if g > 160:
        g = 160
    b = b + 5
    if b > 109:
        b = 109


done()