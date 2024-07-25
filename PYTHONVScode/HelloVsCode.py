import turtle
import random

# Set up the screen
window = turtle.Screen()
window.bgcolor("white")
window.title("Complex Geometric Art")
window.setup(width=800, height=800)

# Create a turtle object
artist = turtle.Turtle()
artist.speed(0)
artist.color("black")
turtle.tracer(0, 0)  # Turn off animation to draw faster

# Draw the complex geometric pattern
for _ in range(36):  # 36 repetitions for a full circle
    for _ in range(100):  # Draw 100 lines for each repetition
        artist.forward(200)
        artist.right(170)
    artist.right(10)  # Rotate for the next repetition

# Hide the turtle and display the artwork
artist.hideturtle()
turtle.update()  # Update the screen

# Keep the window open until the user closes it
turtle.mainloop()