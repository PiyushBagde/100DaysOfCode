from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color('white')
        self.show()
        self.hideturtle()

    def show(self):
        self.write(f"Score = {self.score} ", align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.show()

    def game_over(self):
        self.goto(0,0)
        self.write( 'Game over, Well player! 🥳', align=ALIGNMENT, font=FONT)

