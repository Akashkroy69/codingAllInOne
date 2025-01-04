import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Happy Birthday Nivaan!")

# Function to draw a balloon
def draw_balloon(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(20)  # Balloon size
    t.end_fill()
    t.penup()
    t.goto(x, y - 20)
    t.pendown()
    t.color("black")
    t.setheading(-90)
    t.forward(40)  # Balloon string

# Display message
def display_message():
    t.penup()
    t.goto(0, 200)
    t.color("red")
    t.write("Happy Birthday Nivaan!", align="center", font=("Arial", 24, "bold"))

# Create balloons
def create_balloons():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    for _ in range(15):  # Adjust the number of balloons
        x = random.randint(-200, 200)
        y = random.randint(-100, 100)
        color = random.choice(colors)
        draw_balloon(x, y, color)

# Turtle setup
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Main program
display_message()
create_balloons()

# End program
turtle.done()
