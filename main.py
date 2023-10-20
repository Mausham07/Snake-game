from turtle import Turtle, Screen
from snake import Snake 
from food import Food
from scrore import Score
import time



screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("yellow")
screen.title("Snake Game")
screen.tracer(0)

score = Score()
new_snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(new_snake.up, "Up")
screen.onkeypress(new_snake.left, "Left")
screen.onkeypress(new_snake.down, "Down")
screen.onkeypress(new_snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move()

    # Detect colison with food
    if new_snake.head.distance(food) < 15:
       food.refresh()
       score.increase_score()

    # Detect colison with wall
    if new_snake.head.xcor() > 340 or new_snake.head.xcor() < -340 or new_snake.head.ycor() > 340 or new_snake.head.ycor() < -340 :
        game_on = False
        score.game_over()
  
screen.exitonclick()