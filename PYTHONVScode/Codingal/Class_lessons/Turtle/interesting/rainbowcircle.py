import turtle

t = turtle.Turtle()
t.speed(0)
colors = ["red", "yellow", "green", "blue", "purple", "orange"]

for x in range(12):
    t.pencolor(colors[x % 6])
    t.circle(100)
    t.left(30)

turtle.done()
