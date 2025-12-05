from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")


for i in range(0,3):
    snake = Turtle()
    snake.color("white")
    snake.shape("square")
    snake.shapesize(1,1)
    snake.goto(-20*i,0)














screen.exitonclick()