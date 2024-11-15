from turtle import Turtle, Screen

# Initial positions for the snake body
position = [(0, 0), (-10, 0), (-20, 0)]
# Constants for directions
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
new_screen = Screen()

class Snake:
    def __init__(self):
        self.snake_list = []  # List to hold the snake segments
        self.create_snake()  # Initialize the snake
        self.head = self.snake_list[0]  # The first segment is the head

    def create_snake(self):
        # Create the initial snake body
        for num in position:
            self.add_snake(num)

    def add_snake(self, num):
        # Add a new segment to the snake
        snake = Turtle("square")
        snake.penup()
        snake.speed("fastest")
        snake.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make the snake smaller
        snake.goto(num)
        self.snake_list.append(snake)

    def extend(self):
        # Add a new segment to the end of the snake
        self.add_snake(self.snake_list[-1].position())

    def move(self):
        # Move each segment to the position of the previous one
        for sn in range(len(self.snake_list) - 1, 0, -1):
            x_cordinate = self.snake_list[sn - 1].xcor()
            y_cordinate = self.snake_list[sn - 1].ycor()
            self.snake_list[sn].goto(x_cordinate, y_cordinate)
        self.snake_list[0].forward(10)  # Move the head forward

    def snake_reset(self):
        # Move the snake segments off-screen and reset
        for s in self.snake_list:
            s.goto(1000, 1000)
        self.snake_list.clear()  # Clear the segments
        self.create_snake()  # Recreate the initial snake
        self.head = self.snake_list[0]

    # Change the direction of the snake
    def up(self):
        if self.head.heading() != DOWN:  # Prevent reversing direction
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
