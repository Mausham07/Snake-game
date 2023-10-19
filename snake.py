from turtle import Turtle, Screen
position = [0, -10, -20]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
new_screen = Screen()

class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for num in range(0, 3):
            snake = Turtle("square")
            snake.penup()
            snake.goto(x=position[num], y=0)
            self.snake_list.append(snake)

    def move(self):
        for sn in range(len(self.snake_list)-1, 0, -1):
            x_cordinate = self.snake_list[sn-1].xcor()
            y_cordinate = self.snake_list[sn-1].ycor()
            self.snake_list[sn].goto(x_cordinate, y_cordinate)
        self.snake_list[0].forward(10)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)