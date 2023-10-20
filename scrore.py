from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreboard = 0
        self.penup()
        self.goto(0, 320)
        self.write(f"Scrore: {self.scoreboard}", move=False, align="center", font=("Courier", 20, "normal"))
        self.hideturtle()
    
    def update(self):
        self.write(f"Scrore: {self.scoreboard}", move=False, align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align="center", font=("Courier", 20, "normal"))

    def increase_score(self):
        self.scoreboard += 1
        self.clear()
        self.update()