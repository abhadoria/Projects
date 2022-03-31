# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:46:48 2022

@author: shrih
"""

import turtle as t

size=300
points=5
angle=180-(180/points)

t.color('blue')
t.begin_fill()
for i in range(points):
    t.forward(size)
    t.right(angle)