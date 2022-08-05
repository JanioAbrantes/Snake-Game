from turtle import Turtle
from random import choice

RANDOM_X = [-380, -360, -340, -320, -300, -280, -260, -240, -220, -200, -180, -160, -140,
            -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200,
            220, 240, 260, 280, 300, 320, 340, 360, 380]

RANDOM_Y = [-280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20,
            0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('magenta')
        self.speed('fastest')
        self.goto(choice(RANDOM_X), choice(RANDOM_Y))
