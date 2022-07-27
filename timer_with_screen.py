from turtle import Screen
from timer import Timer_manage
import time
screen=Screen()
screen.setup(600,600)

ti=Timer_manage()
for i in range(10):
    time.sleep(1)
    ti.counter()



screen.exitonclick()