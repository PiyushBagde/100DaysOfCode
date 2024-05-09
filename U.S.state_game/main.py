import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guesses_states = []

while len(guesses_states) <= 50:
    answer_state = screen.textinput(title=f"{len(guesses_states)}/50 : Guess the state",
                                    prompt="Can you guess the state's name? ").title()
    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guesses_states:
                missing_states.append(state)

        df = pandas.DataFrame(missing_states)
        df.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        row = data[data.state == answer_state]
        t.goto(int(row.x), int(row.y))
        t.write(answer_state)
        guesses_states.append(answer_state)
