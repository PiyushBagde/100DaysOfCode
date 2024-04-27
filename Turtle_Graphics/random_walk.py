from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

colors = ["slate blue", 'blue violet', 'deep pink', 'red', 'dark orange', 'aquamarine', 'midnight blue', 'blue',
          'cornflower blue','wheat']

direction = [0, 90, 180, 270]
tim.pensize(10)


def random_walk(steps):
    for _ in range(steps):
        tim.speed("normal")
        tim.setheading(random.choice(direction))
        tim.color(random.choice(colors))
        tim.forward(30)


random_walk(200)

screen.exitonclick()
