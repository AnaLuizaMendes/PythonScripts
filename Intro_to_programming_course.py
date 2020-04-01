# Lesson 1 - Turtle
import turtle

# Making a triangle:
fred = turtle.Turtle()
fred.color("red")
fred.forward(100)
fred.right(135)
fred.forward(140)
fred.right(135)
fred.forward(100)

# Making a square:
fred = turtle.Turtle()
fred.color("blue")
fred.forward(100)
fred.color("red")
fred.right(90)
fred.forward(100)
fred.color("green")
fred.right(90)
fred.forward(100)
fred.color("yellow")
fred.right(90)
fred.forward(100)

# Also making a square:
george = turtle.Turtle()
george.color("yellow")
for side in [1, 2, 3, 4]:
    george.forward(100)
    george.right(90)

# Let's try a five points star (angle inside - 36 degrees):
stella = turtle.Turtle()
stella.color("pink")
for side in range(5):
    stella.forward(100)
    stella.right(144)
