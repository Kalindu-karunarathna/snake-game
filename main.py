from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from score import Score
import winsound

screen = Screen()
screen.setup(width=750,height=750)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


border = Turtle()
border.penup()
border.goto(300,-300)
border.pendown()
border.pencolor("white")
border.pensize(10)
border.hideturtle()
for i in range(4):
    border.left(90)
    border.forward(600)




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
    if score.score<=5:
        time.sleep(0.15)
    elif score.score<=10:
        time.sleep(0.14)
    elif score.score<=15:
        time.sleep(0.13)
    elif score.score<=20:
        time.sleep(0.12)
    elif score.score<=25:
        time.sleep(0.11)
    else:
        time.sleep(0.1)

    snake.move()

    if snake.segments[0].distance(food)<17:
        winsound.PlaySound("sounds/eat.wav", winsound.SND_ASYNC)
        food.refresh()
        score.increase_score()
        snake.extend()

    if (snake.segments[0].xcor()>299 or  snake.segments[0].xcor()<-299 or
            snake.segments[0].ycor()>299 or snake.segments[0].ycor()<-299):
        winsound.PlaySound("sounds/game_over.wav", winsound.SND_ASYNC)
        is_game_on=False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<10:
            winsound.PlaySound("sounds/game_over.wav", winsound.SND_ASYNC)
            is_game_on=False
            score.game_over()






screen.exitonclick()