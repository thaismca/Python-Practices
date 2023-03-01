from turtle import Turtle
import random

class Food(Turtle):
    """Models the food in the Snake Game. It inherities from the Turtle class"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("green")
        self.speed("fastest")
        # reduce the default circle size (20x20) by half (10x10)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # go to a random location inside the screen
        self.refresh_position()

    def refresh_position(self):
        '''Sets new random x and y coordinates and moves the food to that position'''
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
