from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.fillcolor('hot pink')
tim.pencolor('hot pink')

tim.begin_fill()
tim.left(140)
tim.forward(100)

tim.circle(-50,200)
tim.left(120)
tim.circle(-50,200)
tim.forward(100)

tim.end_fill()

screen.exitonclick()