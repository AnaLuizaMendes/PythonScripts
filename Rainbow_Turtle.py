# Rainbow time
import turtle

ray = turtle.Turtle()
rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

ray.speed(3)
ray.width(5)

for rainbow_color in rainbow:
    ray.color(rainbow_color)
    for side in range(5):
        ray.forward(50)
        ray.right(144)
    ray.penup()
    ray.left(60)
    ray.forward(60)
    ray.pendown()

ray.penup()
ray.right(90)
ray.forward(100)
ray.right(90)
ray.forward(50)
ray.right(180)
ray.pendown()

for rainbow_color in rainbow:
    ray.color(rainbow_color)
    ray.forward(100)
    ray.penup()
    ray.right(90)
    ray.forward(5)
    ray.right(90)
    ray.forward(100)
    ray.right(180)
    ray.pendown()
