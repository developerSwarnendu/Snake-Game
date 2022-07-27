from turtle import Screen
import time
from snake import Snake
from Food import Food
from scoreboard import Score
HEAD=0
screen=Screen()

screen.setup(width=600,height=600)
screen.bgcolor('chartreuse')
screen.title("Snake Game created by Swarnendu Chatterjee")
screen.tracer(0)

sn=Snake()
food=Food()
score=Score()


game_is_on=True

screen.listen()
screen.onkey(key="Up",fun=sn.up)
screen.onkey(key="Down",fun=sn.down)
screen.onkey(key="Left",fun=sn.left)
screen.onkey(key='Right',fun=sn.right)
i=3
while game_is_on:
    screen.update()
    time.sleep(0.1)
    sn.move()

    if sn.snake_body[HEAD].distance(food)<14:
        food.move_food()
        sn.add_body()
        score.score_increase()

    if sn.snake_body[HEAD].xcor()>290 or sn.snake_body[HEAD].xcor()< -290 or sn.snake_body[HEAD].ycor()>290 or sn.snake_body[HEAD].ycor()< -290:
        game_is_on=False
        score.gameOver()

    for snake in sn.snake_body[2:]:
        if(sn.snake_body[HEAD].distance(snake)<8):
            game_is_on=False
            score.gameOver()


screen.exitonclick()