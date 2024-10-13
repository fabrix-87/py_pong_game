from turtle import Turtle

INITIAL_SCORE = 0
INCREMENT_SCORE = 1
ALIGNMENT = "center"
FONT = ("Courier", 60, "bold")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()    
        self.reset_score()

    def l_point(self):
        self.l_score += INCREMENT_SCORE
        self.refresh_score()

    def r_point(self):
        self.r_score += INCREMENT_SCORE
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align=ALIGNMENT,font=FONT)
        self.goto(100,200)
        self.write(self.r_score,align=ALIGNMENT,font=FONT)

    def reset_score(self):
        self.l_score = INITIAL_SCORE
        self.r_score = INITIAL_SCORE
        self.refresh_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)