from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.4,stretch_wid=0.4)
        self.color('blue')
        self.penup()
        self.speed(0)
        self.move_food()

    def move_food(self):
        x_axix=random.randint(-280,280)
        y_axix=random.randint(-280,280)
        self.goto(x_axix,y_axix)
    
