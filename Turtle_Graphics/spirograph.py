import turtle as t
import random

tim = t.Turtle()


tim.speed('fastest')
t.colormode(255)


colors = ["slate blue", 'blue violet', 'deep pink', 'red', 'dark orange', 'aquamarine', 'midnight blue', 'blue',
          'cornflower blue','wheat']

def random_color():
    """Returns a random pastel RGB color tuple."""
    r = random.randint(75, 255)
    g = random.randint(75, 255)
    b = random.randint(75, 255)
    color = (r, g, b)
    return color

def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random.choice(colors))
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
