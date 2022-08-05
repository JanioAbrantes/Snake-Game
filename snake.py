from turtle import Turtle
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.minhoca = []
        self.create_snake()
        self.head = self.minhoca[0]

    def create_snake(self):
        for position in START_POSITIONS:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.minhoca.append(segment)

    def eat(self):
        self.minhoca.append(self.minhoca[-1].clone())


    def move(self):
        for parte in range(len(self.minhoca) - 1, 0, -1):
            new_x = self.minhoca[parte - 1].xcor()
            new_y = self.minhoca[parte - 1].ycor()
            self.minhoca[parte].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
