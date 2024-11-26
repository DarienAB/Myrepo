import time
from turtle import Screen
from player import Player, STARTING_POSITION, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

car_manager = CarManager()

player = Player()
screen.listen()
screen.onkey(player.go_up,"Up")
game_is_on = True

scoreboard = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    #Detect successful crossing
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_score()

screen.exitonclick()