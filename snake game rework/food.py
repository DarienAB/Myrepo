import random
from turtle import Turtle
class Food(Turtle): # This calls the class that we want to use
    def __init__(self):
       super().__init__()
       self.shape("circle")
       self.penup()
       self.shapesize(stretch_len=0.5, stretch_wid=0.5)#This creates a 10 by 10 circle. The original size was 20 by 20 pixels
       self.color("blue")
       self.speed("fastest")
       self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
