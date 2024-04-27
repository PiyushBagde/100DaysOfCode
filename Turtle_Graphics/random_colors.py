import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()

t.colormode(255)
tim.speed("normal")
direction = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("normal")


def random_color():
    """Returns a random pastel RGB color tuple."""
    r = random.randint(75, 255)
    g = random.randint(75, 255)
    b = random.randint(75, 255)
    color = (r, g, b)
    return color


def random_walk(steps):
    for _ in range(steps):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(direction))


random_walk(200)
screen.exitonclick()
