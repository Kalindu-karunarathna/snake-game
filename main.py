from turtle import Turtle,Screen
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions=[(0,0),(-20,0),(-40,0)]
segments =[]


for i in starting_positions:
    snake = Turtle()
    snake.color("white")
    snake.shape("square")
    snake.shapesize(1,1)
    snake.penup()
    snake.goto(i)
    segments.append(snake)


is_game_on =True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(segments)-1,0,-1):
        new_x_coordinate = segments[i-1].xcor()
        new_y_coordinate = segments[i-1].ycor()
        segments[i].goto(new_x_coordinate,new_y_coordinate)

    segments[0].forward(20)







screen.exitonclick()