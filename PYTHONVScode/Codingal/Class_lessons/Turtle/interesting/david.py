import turtle
import colorsys

# Setup the turtle screen
turtle.bgcolor('black')
t = turtle.Turtle()
t.speed(0)  # Set the speed to the fastest

# Number of repetitions
n = 50

# Color setup (using HSV for a smooth transition between colors)
hue = 0.0
turtle.colormode(1.0)

for i in range(100):
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(color)
    t.forward(i * 2)
    t.left(90)
    t.forward(i * 2)
    t.left(90)
    t.forward(i * 2)
    t.left(90)
    t.forward(i * 2)
    t.left(95)  # Change direction slightly for each iteration
    hue += 1/n  # Change color slightly

# Hide turtle after completion
t.hideturtle()

# Keep the window open
turtle.done()
