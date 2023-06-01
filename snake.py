from turtle import Turtle ,Screen
from scoreboard import Gameover
# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_CORDINATES = [0, -20, -40]
MOVE_DISTANCE = 10
# RANGE = n



class Snake:
    def __init__(self):
      self.game_on = True
      self.snake_size = []
      self.create_snake()
      
    def create_snake(self):
      
        for snake in range(3):
            self.add_snake(snake)
     
    def add_snake(self,snake):
            i = 0
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(x=SNAKE_CORDINATES[i], y=0)
            self.snake_size.append(snake)
            i += 1
     
    def extend(self):
            self.add_snake(self.snake_size[-1].position())
            
    def move(self):
        for snk in range(len(self.snake_size) - 1, 0, -1):
            new_x = self.snake_size[snk - 1].xcor()
            new_y = self.snake_size[snk - 1].ycor()
            self.snake_size[snk].goto(new_x,new_y)
            self.snake_size[0].fd(MOVE_DISTANCE)
            
  
            
    def move_left(self):
          self.snake_size[0].left(90) 
    def move_right(self):
          self.snake_size[0].right(90) 
    
    def check_cordinates(self):
        if self.snake_size[0].xcor() >= 300 or  self.snake_size[0].xcor() <= -300 or self.snake_size[0].ycor() >= 300 or  self.snake_size[0].ycor() <= -300:
            self.game_on = False
            self.snake_size[0] = Gameover()
       
          
    
        