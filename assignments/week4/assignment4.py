# import
import turtle as t

# 1. square (purple)
t.color("purple")
t.pensize(5)
for i in range(4):
    t.forward(100)
    t.right(90)

# changing spot
t.penup()
t.goto(-150, 0) # hopping to the left
t.pendown()

# 2. triangle (orange)
t.color("orange")
for i in range(3):
    t.forward(100)
    t.left(120) # equilateral triangle

# changing sport
t.penup()
t.goto(150, 0) # hopping to the right
t.pendown()

# 3. circle (green)
t.color("green")
t.circle(50) # drawing a circle (radius 50)

t.done()