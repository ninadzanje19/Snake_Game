from turtle import Turtle
ALINGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score: {self.score}", align=ALINGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALINGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("blue")
        self.write("GAME OVER :(", align=ALINGNMENT, font=("Arial", 24, "normal"))
