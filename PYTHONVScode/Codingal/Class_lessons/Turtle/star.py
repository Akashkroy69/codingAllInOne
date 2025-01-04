# import turtle

# # print(6%3)

# turtleObj = turtle.Turtle()
# turtleObj.pensize(5)

# # set up our window
# window = turtle.Screen()
# window.title("Triangle")
# window.bgcolor("green")
# window.setup(500, 500)
# color = [
# "red", "blue", "yellow"
# ]

# side = 10
# for i in range(100):b
#   side += 10
#   turtleObj.forward(side)
#   turtleObj.right(60)
#   turtleObj.pencolor(color[i%len(color)])

# turtle.done()


import turtle

t = turtle.Turtle()
t.speed(0)
colors = ["red", "yellow", "green", "blue", "purple", "orange"]
for x in range(100):
    t.color(colors[x % 6])
    t.begin_fill()
    
    t.forward(5*x)
    t.left(170)
    t.end_fill()

turtle.done()