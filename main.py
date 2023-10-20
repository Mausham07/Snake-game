from turtle import Turtle, Screen
from snake import Snake 
from food import Food
import time


screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("yellow")
screen.title("Snake Game")
screen.tracer(0)

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
    

    if new_snake.head.distance(food) < 15:
       food.refresh()

  
screen.exitonclick()