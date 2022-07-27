import imp
from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()
tim.penup()
tim.hideturtle()
screen.setup(width=600,height=600)
tim.speed(0)
tim.goto(0,278)
tim.write(f"Score:{0}", False, align="center",font=('Arial',12,'normal'))
tim.clear()
tim.write(f"Score:{1}", False, align="center",font=('Arial',12,'normal'))

screen.exitonclick()