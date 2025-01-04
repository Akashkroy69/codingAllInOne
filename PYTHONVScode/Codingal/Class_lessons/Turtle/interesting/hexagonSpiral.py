import turtle

t = turtle.Turtle()
t.speed(0)
colors = ["red", "yellow", "blue", "green", "purple", "orange"]

for i in range(360):
    t.pencolor(colors[i % 6])
    t.forward(i * 2)
    t.left(59)

turtle.done()
