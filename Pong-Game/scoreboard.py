from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align='center', font=('Courier', 80, "normal"))

        self.goto(100, 180)
        self.write(self.r_score, align='center', font=('Courier', 80, "normal"))

    def update_l_score(self):
        self.l_score += 1
        self.update_score()

    def update_r_score(self):
        self.r_score += 1
        self.update_score()
