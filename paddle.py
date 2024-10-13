from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position: str = 'right') -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if(position == 'right'):
            self.goto(360,0)
        else:
            self.goto(-360,0)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)
    
    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
