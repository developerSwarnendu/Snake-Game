from turtle import Turtle

class Timer_manage(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.val=0
        self.penup()
        self.hideturtle()
        self.goto(230,280)
        # self.color('white')
        self.write(f"Timer={self.val}",False,align='center',font=('Courier',15,'normal'))

    def counter(self):
        self.val+=1
        self.clear()
        self.write(f"Timer={self.val}",False,align='center',font=('Courier',15,'normal'))
        