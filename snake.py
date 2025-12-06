from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


#snake class use to create snake on the starting position when game starts,
#move method use to move the snake such that all the segments follow the 1 segment which act like head
#extend method use to increase the length of snake when eat food
#up,down.left,right methods use to turn the snake base on the key press by the user.
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

    def extend(self):
        snake = Turtle()
        snake.color("white")
        snake.shape("square")
        snake.shapesize(1, 1)
        snake.penup()
        x_coordinate = self.segments[len(self.segments)-1].xcor()
        y_coordinate = self.segments[len(self.segments) - 1].ycor()
        snake.goto(x_coordinate,y_coordinate)
        self.segments.append(snake)

    def up(self):
        if self.segments[0].heading()!= DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

