from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.starting_positions= STARTING_POSITIONS
        self.segments =[]

        for i in self.starting_positions:
            snake = Turtle()
            snake.color("white")
            snake.shape("square")
            snake.shapesize(1, 1)
            snake.penup()
            snake.goto(i)
            self.segments.append(snake)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x_coordinate = self.segments[i - 1].xcor()
            new_y_coordinate = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x_coordinate, new_y_coordinate)

        self.segments[0].forward(MOVE_DISTANCE)
