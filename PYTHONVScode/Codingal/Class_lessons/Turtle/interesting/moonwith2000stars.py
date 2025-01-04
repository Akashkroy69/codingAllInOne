# import pygame
# pygame.init()
# lastP = pygame.time.get_ticks()
# print(lastP)
# while True:
#    pygame.time.Clock().tick(1)
#    # OR, pygame.time.wait(1000)
#    timeNow = pygame.time.get_ticks()
#    print("TIME NOW :------",timeNow)
#    if timeNow - lastP > 1500:      
#       print(timeNow,lastP)
#       lastP = timeNow
#       print(timeNow)
import turtle
import random
from PIL import Image
t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800,600)
# list=["white","green","purple","yellow","blue","purple"]
list=["white","white","white","white","white","white"]
# Draw the semi-circle (half moon shape)
t.speed(10)
t.goto(-300,100)
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)  # Draw a semi-circle
# t.left(90)          # Turn to close the shape
# t.forward(200)      # Draw the straight edge
# t.left(90)          # Turn again
# t.circle(100, -180) # Draw another semi-circle
t.end_fill()
t.pencolor("white")
t.penup()
x=-200
y=-200
t.goto(x,y)
t.pendown()
for j in range(2000):
  t.penup()
  t.goto(random.randint(-200,400),random.randint(-300,300))
  t.pendown()
  t.forward(1)
  if j%10==0:
      t.penup()
      t.goto(random.randint(-400,-200),random.randint(-300,100))
      t.pendown()
      t.forward(1)
#   for i in range(3):
#     t.pencolor(list[i%len(list)])
#    #  t.circle(2)
#     t.forward(2)
#     t.left(144)

# for saving 
# canvas = turtle.getcanvas()
# canvas.postscript(file="drawing.eps")

# image = Image.open("drawing.eps")
# image.save("drawing.png")

turtle.done()