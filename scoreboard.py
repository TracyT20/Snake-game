from turtle import Turtle
with open("High_score.txt","r") as f:
    HIGH_SCORE=f.read()

ALIGNMENT="center"
FONT= ("courier", 18, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.High_score=int(HIGH_SCORE)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()
    def update_score(self):
        self.write(f"Score : {self.score}   High score : {self.High_score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        if self.score > self.High_score:
            self.High_score = self.score
            self.clear()
            self.update_score()
            with open("High_score.txt","w") as file:
                file.write(str(self.High_score))
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
    def track_score(self):
        self.score+=1
        self.clear()
        self.update_score()


