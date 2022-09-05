from turtle import Turtle

""" GLOBALS """
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []  # List of Squares
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)

    def add_segment(self, position):
        """ For Drawing Snake """
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):  # Erkaracnel
        self.add_segment(self.segments[-1].position())

    def move(self):
        for s in range(len(self.segments) - 1, 0, -1):  # start=len(segments) - 1, stop=0, step=-1
            new_x = self.segments[s - 1].xcor()
            new_y = self.segments[s - 1].ycor()
            self.segments[s].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)  # Change direction to 90 angle

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)  # Change direction to 270 angle

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)  # Change direction to 180 angle

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)  # Change direction to 0 angle

