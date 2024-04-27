import turtle as t
import random
import colorgram

tim = t.Turtle()
tim.penup()
tim.speed('fastest')
tim.hideturtle()


def get_colors(colors):
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors = (r, g, b)
        color_list.append(rgb_colors)


def draw_line(no_of_dots, dot_size, gap):
    for _ in range(no_of_dots):
        tim.dot(dot_size, random.choice(color_list))
        tim.forward(gap)


def draw_painting(painting_size, dot_size, gap):
    y_coordinate = -200
    tim.setpos(-200, -200)
    for _ in range(painting_size):
        draw_line(painting_size, dot_size, gap)
        y_coordinate += 50
        tim.setpos(-200, y_coordinate)


colors = colorgram.extract('img.png', 30)
color_list = []

get_colors(colors)
t.colormode(255)

draw_painting(10, 20, 50)

screen = t.Screen()
screen.exitonclick()
