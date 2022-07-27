from turtle import Turtle

class Snake:
    count=2
    snake_body=[]
    def __init__(self) -> None:
        # self.speed=3
        for i in range(3):
            if(i==0):
                self.snake_body.append(Turtle(shape='square'))
            else:
                self.snake_body.append(Turtle(shape='square'))
            self.snake_body[i].color('black')
            # self.snake_body[i].speed(self.speed)
            # snake_body[i].resizemode('user')
            self.snake_body[i].shapesize(stretch_wid=0.75,stretch_len=0.75)
            self.snake_body[i].penup()
            if(i!=0):
                self.snake_body[i].backward(i*10)


    def move(self):
    # move of the snake including left and right turn
        for move in range(len(self.snake_body)-1,0,-1):
            prev=self.snake_body[move-1]
            x_cor=prev.xcor()
            y_cor=prev.ycor()
            self.snake_body[move].goto(x_cor,y_cor)
        self.snake_body[0].fd(10)

    def up(self):
        if self.snake_body[0].heading()!=270:
            self.snake_body[0].setheading(90)
    
    def down(self):
        if self.snake_body[0].heading()!=90:
            self.snake_body[0].setheading(270)
    
    def left(self):
        if self.snake_body[0].heading()!=0:
            self.snake_body[0].setheading(180)

    def right(self):
        if self.snake_body[0].heading()!=180:
            self.snake_body[0].setheading(0)

    def add_body(self):
        self.count+=1
        self.snake_body.append(Turtle(shape='square'))
        self.snake_body[self.count].color('black')
        self.snake_body[self.count].shapesize(stretch_wid=0.75,stretch_len=0.75)
        self.snake_body[self.count].penup()
        self.snake_body[self.count].backward(self.count*10)