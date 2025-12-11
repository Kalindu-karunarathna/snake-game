from turtle import Turtle

#score class use to calculate the score and display it,
#and finally display the 'Game Over!' when the snake collide.
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,325)
        self.hideturtle()
        self.score = 0
        self.high_score =0
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align="center", font=("Courier New",24,"normal"))

    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align="center", font=("Courier New", 24, "normal"))

    #reset the game and track the high score
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score =0
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align="center",
                   font=("Courier New", 24, "normal"))
        # self.increase_score()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!", align="center", font=("Courier New", 24, "normal"))
