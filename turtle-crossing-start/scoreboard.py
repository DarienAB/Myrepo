from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-230,275)
        self.update()

    def update(self): # This has the score
        self.write(f"Level: {self.score} ", False, "center", FONT )

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update()
    def game_over(self):
        self.penup()
        self.hideturtle()  # This hides the turtle it creates
        self.goto(0, 0)
        self.write("GAME OVER.", False, "center", FONT)


