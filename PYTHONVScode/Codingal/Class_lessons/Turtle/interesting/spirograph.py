import turtle

t = turtle.Turtle()
t.speed(0)
# for j in range(3):
for i in range(360):
    t.width(i//100)
    t.circle(100)
    t.right(10)

turtle.done()
