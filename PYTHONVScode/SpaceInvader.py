import turtle
import time
import random

# Set up the screen
window = turtle.Screen()
window.title("Space Invaders")
window.bgcolor("black")
window.setup(width=800, height=600)

# Create the player's spaceship
player = turtle.Turtle()
player.shape("triangle")
player.color("blue")
player.penup()
player.goto(0, -250)
player.speed(0)

# Create the bullet
bullet = turtle.Turtle()
bullet.shape("triangle")
bullet.color("yellow")
bullet.penup()
bullet.speed(0)
bullet.goto(0, -240)
bullet.hideturtle()
bullet_state = "ready"

# Set bullet speed
bullet_speed = 20

# Create enemy invaders
enemies = []
for _ in range(5):
    enemy = turtle.Turtle()
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    x = random.randint(-380, 380)
    y = random.randint(100, 250)
    enemy.goto(x, y)
    enemies.append(enemy)

# Set enemy speed
enemy_speed = 5

# Function to move the player left
def move_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

# Function to move the player right
def move_right():
    x = player.xcor()
    x += 20
    player.setx(x)

# Function to shoot the bullet
def shoot_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.goto(x, y)
        bullet.showturtle()

# Keyboard bindings
window.listen()
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(shoot_bullet, "space")

# Main game loop
while True:
    window.update()

    # Move the bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

        # Check if bullet reaches the top
        if bullet.ycor() > 290:
            bullet.hideturtle()
            bullet_state = "ready"
