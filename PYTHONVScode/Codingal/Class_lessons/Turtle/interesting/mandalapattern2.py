import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
for i in range(1000):
    t.pencolor(colors[i % 6])
    t.circle(i%100)
    t.left(10)

    

turtle.done()
