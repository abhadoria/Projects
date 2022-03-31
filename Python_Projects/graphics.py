# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:36:37 2022

@author: shrih
"""

import turtle as t
def rectangle(horizontal,vertical,color):
    t.pendown()
    t.pensize(2)
    t.color(color)
    t.begin_fill()
    for i in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
    t.speed('fast')
    t.bgcolor("Grey")


t.goto(-100,-150)
rectangle(50,20,"Purple")
t.goto(-30,-150)
rectangle(50,20,"Purple")

t.goto(-25,-50)
rectangle(15,100,"red")
t.goto(-55,-50)
rectangle(-15,100,"red")

t.goto(-90,100)
rectangle(100,150,'red')

t.goto(-150,70)
rectangle(60,15,"gold")
t.goto(-150,110)
rectangle(15,40,"gold")

t.goto(10,70)
rectangle(60,15,"gold")
t.goto(55,110)
rectangle(15,40,"gold")

t.goto(-50,120)
rectangle(15,20,'black')

t.goto(-85,170)
rectangle(80,50,'red')

t.goto(-60,160)
rectangle(30,10,"blue")
t.goto(-55,155)
rectangle(5,5,"yellow")
t.goto(-40,155)
rectangle(5,5,"yellow")

t.goto(-65,135)
rectangle(40,5,"yellow")

t.hideturtle()