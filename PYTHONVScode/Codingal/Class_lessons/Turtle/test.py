import turtle
import math
import random

#arrow
arrow = turtle.Turtle()
arrow.speed(0)
arrow.pensize(3)
#index:    1        2        3       4       5      6
color = ["red", "orange", "blue", "pink", "green"]
for i in range(500):
    print("i: ", i)
    arrow.pencolor(color[random.randint(0,4)])
    arrow.forward(i)
    arrow.left(i)
turtle.done()