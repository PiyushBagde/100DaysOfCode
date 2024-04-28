from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
# screen.textinput(title='whom do you love? ', prompt='i love')
user_bet = screen.textinput(title='Make your Bet', prompt="Which turtle will win the race <3"
                                                          " Enter the color ('red', 'blue', 'green', 'yellow', 'purple'): ")
colors = ['red', 'blue', 'green', 'yellow', 'purple']
y_coordinates = [-100, -50, 0, 50, 100]
all_turtles = []

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape='turtle')
    all_turtles.append(new_turtle)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinates[turtle_index])

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 215:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You ve won the {winning_color} turtle is the winner!')
            else:
                print(f'yooy loose the {winning_color} turtle is the winner!')
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
