import turtle
t = turtle.Turtle()
t.speed(0)
t.color("red")

for i in range(36):
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)

turtle.done()
