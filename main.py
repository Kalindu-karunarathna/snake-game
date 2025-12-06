from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=660,height=660)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


border = Turtle()
border.penup()


snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

score = Score()


is_game_on =True

while is_game_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    if snake.segments[0].distance(food)<15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if (snake.segments[0].xcor()>280 or  snake.segments[0].xcor()<-280 or
            snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280):
        is_game_on=False
        score.game_over()

    for segment in snake.segments:
        if segment==snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment)<10:
            is_game_on=False
            score.game_over()






screen.exitonclick()