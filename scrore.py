from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        # Read high score from file
        with open("high_score.txt") as r_file:
            self.high_score = r_file.read()
        self.scoreboard = 0
        self.penup()
        self.goto(0, 320)  # Position the score display at the top
        self.hideturtle()
        self.update()  # Update the score display

    def update(self):
        # Clear the old score and display the new one
        self.clear()
        self.write(f"Score: {self.scoreboard} High score: {self.high_score}", move=False, align="center", font=("Courier", 20, "normal"))

    def game_reset(self):
        # Update high score if the current score is greater
        if self.scoreboard > int(self.high_score):
            self.high_score = self.scoreboard
        self.scoreboard = 0  # Reset current score
        self.update()
        # Save the high score to file
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def increase_score(self):
        self.scoreboard += 1  # Increment score
        self.update()  # Update score display
