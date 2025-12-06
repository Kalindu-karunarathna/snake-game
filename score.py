from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,325)
        self.hideturtle()
        self.score = 0
        self.write(f"Score : {self.score} ", align="center", font=("Courier New",24,"normal"))

    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score : {self.score} ", align="center", font=("Courier New", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=("Courier New", 24, "normal"))
