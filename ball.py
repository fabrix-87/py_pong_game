from turtle import Turtle
import random

MOVE_DISTANCE = 5

class Ball(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape('circle')
        self.color('white')
        self.shapesize(1,1)
        #self.speed("fastest")
        self.penup()
        #starting_angle = random.randint(0,3) * 90 + 45
        #self.setheading(starting_angle)
        sign_x = -1 if random.randint(0,1) < 1 else 1
        sign_y = -1 if random.randint(0,1) < 1 else 1
        self.x_move = 10 * sign_x
        self.y_move = 10 * sign_y       

        self.respawn()

    def respawn(self):
        self.ball_speed = 1
        self.bounce_x()
        self.goto(0,random.randint(-250,250))

    def move(self):                 
        new_x = self.xcor() + self.x_move * self.ball_speed
        new_y = self.ycor() + self.y_move * self.ball_speed
        self.goto(new_x, new_y)
        
    def bounce_wall(self):
        #rimbalza
        if(self.ycor() > 0 and self.xcor() > 0) or (self.ycor() < 0 and self.xcor() < 0):
            self.setheading(self.heading() - 90)
        else:
            self.setheading(self.heading() + 90)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def increase_speed(self):
        self.ball_speed *= 1.5