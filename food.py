from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        # Food appearance settings
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Makes the food smaller
        self.color("blue")
        self.speed("fastest")
        self.refresh()  # Randomly place food on initialization

    def refresh(self):
        # Randomly generate new coordinates for the food
        random_x = random.randint(-330, 310)
        random_y = random.randint(-330, 310)
        self.goto(random_x, random_y)
