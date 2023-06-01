from turtle import Turtle , Screen
from food import Food
from snake import Snake
import random
from scoreboard import Scoreboard
import time

score = Scoreboard()
# score.n = 0

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snakeZ")
screen.tracer(0)

saap = Snake()
food = Food()
screen.listen()

#single tap moving .   .    .   .
screen.onkey(key="a",fun=saap.move_left)
screen.onkey(key="d",fun=saap.move_right)




# saap.game_ona
while saap.game_on:
    screen.update()
    time.sleep(0.1)
    saap.move()
    saap.check_cordinates()
  

    if saap.snake_size[0].distance(food) < 15 : 
        
        food.refresh()
        saap.extend()
        score.increase_score()
       


screen.exitonclick()
 