import turtle
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times New Roman", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
           self.high_score = int(data.read())
        self.color("white") #This turns the color of the scoreboard white
        self.penup()
        self.hideturtle() #This hides the turtle it creates
        self.goto(0, 275)
        self.update()

    def update(self): # This has the score
        self.clear()  # This clears what was previously on there
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT )

    def increment_score(self):
        self.score+=1 #This increments the score by one
        self.update() #This updates the score again

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0

    #def game_over(self):
        #self.penup()
        #self.hideturtle()  # This hides the turtle it creates
        #self.goto(0, 0)
        #self.write("GAME OVER.", False, ALIGNMENT, FONT)



