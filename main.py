from turtle import Screen
from snake import Snake 
from food import Food
from scrore import Score
import time



screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("yellow")
screen.title("Snake Game")
screen.tracer(0)

new_score = Score()
new_snake = Snake()
new_food = Food()

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
    if new_snake.head.distance(new_food) < 15:
       new_food.refresh()
       new_snake.extend()
       new_score.increase_score()

    # Detect colison with wall
    if new_snake.head.xcor() > 340 or new_snake.head.xcor() < -340 or new_snake.head.ycor() > 340 or new_snake.head.ycor() < -340 :
        game_on = False
        new_score.game_over()

    # detect colision of tail
    for seg in new_snake.snake_list[1:]:
        if new_snake.head.distance(seg) < 5:
            game_on = False
            new_score.game_over()
  
screen.exitonclick()