from turtle import Screen
from snake import Snake
from food import Food
from scrore import Score
import time

# Setup the game screen
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("yellow")
screen.title("Snake Game")
screen.tracer(0)  # Turns off animation for smoother game updates

# Create game objects: score, snake, and food
new_score = Score()
new_snake = Snake()
new_food = Food()

# Setup key listeners for controlling the snake
screen.listen()
screen.onkeypress(new_snake.up, "Up")
screen.onkeypress(new_snake.left, "Left")
screen.onkeypress(new_snake.down, "Down")
screen.onkeypress(new_snake.right, "Right")

# Main game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)  # Slow down the game for a smoother experience
    new_snake.move()

    # Detect collision with food
    if new_snake.head.distance(new_food) < 15:
        new_food.refresh()  # Move the food to a random location
        new_snake.extend()  # Extend the snake
        new_score.increase_score()  # Update the score

    # Detect collision with walls
    if (
        new_snake.head.xcor() > 340 or new_snake.head.xcor() < -340 or
        new_snake.head.ycor() > 340 or new_snake.head.ycor() < -340
    ):
        new_score.game_reset()  # Reset score
        new_snake.snake_reset()  # Reset snake position and size

    # Detect collision with the snake's own tail
    for seg in new_snake.snake_list[1:]:
        if new_snake.head.distance(seg) < 5:
            new_score.game_reset()  # Reset score
            new_snake.snake_reset()  # Reset snake position and size

# Exit on screen click
screen.exitonclick()
