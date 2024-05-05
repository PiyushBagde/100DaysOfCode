from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

COLORS = ["slate blue", 'blue violet', 'deep pink', 'red', 'dark orange', 'aquamarine', 'midnight blue', 'blue',
          'cornflower blue']


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # create snake body
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        """Add segment to the snake"""
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color('white')
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
