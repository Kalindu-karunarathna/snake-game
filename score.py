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
        with open("high_score.txt", mode="r") as file:
            content = int(file.read())
        self.high_score =content
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align="center", font=("Courier New",24,"normal"))

    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align="center", font=("Courier New", 24, "normal"))

    #reset the game and track the high score
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score =0
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align="center",
                   font=("Courier New", 24, "normal"))





