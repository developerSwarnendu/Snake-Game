from turtle import Turtle

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score=0
        self.penup()
        self.color('red')
        self.hideturtle()
        self.speed(0)
        self.goto(0,270)
        self.update_score()
        
    def score_increase(self):
        self.score+=1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"Score:{self.score}", False, align="center",font=('Courier',15,'normal'))

    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over", False, align="center",font=('Courier',15,'normal'))
        


        