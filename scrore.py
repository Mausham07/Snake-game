from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt") as r_file:
            self.high_score = r_file.read()
        self.scoreboard = 0
        self.penup()
        self.goto(0, 320)
        self.hideturtle()
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"Scrore: {self.scoreboard} High score: {self.high_score}" , move=False, align="center", font=("Courier", 20, "normal"))

    def game_reset(self):
        if self.scoreboard > int(self.high_score):
            self.high_score = self.scoreboard
        self.scoreboard = 0
        self.update()
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", move=False, align="center", font=("Courier", 20, "normal"))

    def increase_score(self):
        self.scoreboard += 1 
        self.update()