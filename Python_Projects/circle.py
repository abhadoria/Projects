import turtle as t
from itertools import cycle
color=cycle(['red','green','grey','yellow','blue','orange'])
def drawCircle(size,angle,shift):
    t.pencolor(next(color))
    t.circle(size)
    t.forward(shift)
    t.right(angle)
    drawCircle(size+10,angle+1,shift+1)


t.bgcolor("Lawn green")
t.speed('fast')
t.pensize(2)
drawCircle(30,0,1)