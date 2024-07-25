import turtle

turtleObject = turtle.Turtle()
# triangle 1
turtleObject.color("red")
turtleObject.forward(100)
turtleObject.left(120)
turtleObject.color("blue")
turtleObject.forward(100)
turtleObject.left(120)
turtleObject.color("green")
turtleObject.forward(100)

# triangle 2

turtleObject.right(60)
turtleObject.penup()

turtleObject.forward(100)
turtleObject.pendown()
turtleObject.forward(100)
turtleObject.right(120)
turtleObject.forward(100)
turtleObject.right(120)
turtleObject.forward(100)
turtleObject.right(120)
turtle.done()


