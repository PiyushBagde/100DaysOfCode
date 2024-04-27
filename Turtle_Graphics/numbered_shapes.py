from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.shape('arrow')

colors = ["slate blue", 'blue violet', 'deep pink', 'red', 'dark orange', 'aquamarine', 'midnight blue', 'blue',
          'cornflower blue']


def draw(side):
    angle = 360 / side
    tim.color(random.choice(colors))

    for turn in range(side):
        tim.forward(50)
        tim.right(angle)


for side in range(3, 11):
    draw(side)

screen.exitonclick()
