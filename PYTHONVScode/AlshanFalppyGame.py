import turtle
import random

# Set up the game window
window = turtle.Screen()
window.title("Flappy Bird")
window.bgcolor("skyblue")
window.setup(width=800, height=600)
window.tracer(0)

# Bird
bird = turtle.Turtle()
bird.shape("square")
bird.color("yellow")
bird.penup()
bird.goto(-100, 0)

# Gravity
gravity = -0.2

# Functions for bird movement
def flap():
    bird.sety(bird.ycor() + 40)

# Set up keyboard controls
window.listen()
window.onkeypress(flap, "space")

# Generate Pipes
pipes = []
def create_pipe():
    pipe_height = random.randint(50, 250)
    pipe_top = turtle.Turtle()
    pipe_top.shape("square")
    pipe_top.color("green")
    pipe_top.shapesize(stretch_wid=pipe_height/20, stretch_len=3)
    pipe_top.penup()
    pipe_top.goto(400, 300)

    pipe_bottom = turtle.Turtle()
    pipe_bottom.shape("square")
    pipe_bottom.color("green")
    pipe_bottom.shapesize(stretch_wid=pipe_height/20, stretch_len=3)
    pipe_bottom.penup()
    pipe_bottom.goto(400, -300)

    pipes.append((pipe_top, pipe_bottom))

# Main game loop
score = 0
while True:
    window.update()
    
    bird.sety(bird.ycor() + gravity)
    
    # Generate pipes every 200 frames
    if score % 200 == 0:
        create_pipe()

    # Move pipes to the left
    for pipe_top, pipe_bottom in pipes:
        pipe_top.setx(pipe_top.xcor() - 2)
        pipe_bottom.setx(pipe_bottom.xcor() - 2)

    # Check for collisions with pipes or the ground
    for pipe_top, pipe_bottom in pipes:
        if bird.distance(pipe_top) < 20 or bird.distance(pipe_bottom) < 20:
            print("Game Over")
            exit()

        if bird.ycor() < -290:
            print("Game Over")
            exit()

    # Remove off-screen pipes and update the score
    pipes = [(pipe_top, pipe_bottom) for pipe_top, pipe_bottom in pipes if pipe_top.xcor() > -400]
    score += 1

# Keep the window open until manually closed by the user
turtle.done()
