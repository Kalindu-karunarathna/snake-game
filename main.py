from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600,height=630)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

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
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food)<15:
        food.refresh()
        score.increase_score()






screen.exitonclick()