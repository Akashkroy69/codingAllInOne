import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Happy Birthday, Nivaan!")

# Function to draw a balloon
def draw_balloon(x, y, color):
    balloon = turtle.Turtle()
    balloon.hideturtle()
    balloon.penup()
    balloon.goto(x, y)
    balloon.pendown()
    balloon.color(color)
    balloon.begin_fill()
    balloon.circle(30)  # Balloon shape
    balloon.end_fill()

    balloon.penup()
    balloon.goto(x, y - 30)
    balloon.pendown()
    balloon.width(2)
    balloon.color("black")
    balloon.goto(x, y - 70)


colors = ["red", "yellow", "blue", "green", "purple", "orange"]
for _ in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-150, 150)
    color = random.choice(colors)
    draw_balloon(x, y, color)


message = turtle.Turtle()
message.hideturtle()
message.penup()
message.goto(0, 200)
message.color("darkblue")
message.write("Happy Birthday, Nivaan! the Super Intelligent kid!!", align="center", font=("Arial", 24, "bold"))


turtle.done()