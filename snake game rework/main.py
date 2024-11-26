# Import necessary modules from turtle and time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen with dimensions, background color, and title
screen = Screen()
screen.setup(width=600, height=600)  # Screen size
screen.bgcolor("black")  # Background color
screen.title("My Snake Game")  # Title of the game window
screen.tracer(0)  # Turn off screen animation to manually update later

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for key presses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Initialize a flag to control the game loop
game_is_on = True

# Game loop
while game_is_on:
    screen.update()  # Update the screen to show any changes
    time.sleep(0.1)  # Pause for a moment to control the speed of the game
    snake.move()  # Move the snake


    # Detect collision with food
    if snake.head.distance(food) < 15:  # 15 pixels for collision distance
        food.refresh() # Refreshes the food after collision
        snake.extend()# This makes the snake grow and extend
        scoreboard.increment_score()  # This increments the score

    if snake.head.xcor() > 300 or snake.head.xcor() < -300  or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()
    #detected collision with tail
    #if head collides with any segment in the tail:
        #trigger game over sequence
    for segment in snake.segments[1:]: # By slicing the list of segments we can get everything from the list besides the head
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# Exit the game when the screen is clicked
screen.exitonclick()
