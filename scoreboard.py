from turtle import Turtle , Screen


class Scoreboard:
    
    def __init__(self):
        self.n = 0
        self.score = Turtle()
        # screen = Screen()
        self.score.hideturtle()
        self.score.penup()
        self.score.color("white")
        self.score.setposition(0,270)
        
        self.score.write(f"Score:{self.n} ",False,align="center" ,font=('Arial',15,'bold'))

        # score.write("Home = ", True, align="center")

        # screen.exitonclick()
    def update_scoreboard(self):
        self.score.write(f"Score:{self.n} ",False,align="center" ,font=('Arial',15,'bold'))

    def increase_score(self):
        self.n += 1
        self.score.clear()
        self.update_scoreboard()
        
class Gameover(Scoreboard):
    def __init__(self):
        super().__init__()
        self.score.goto(0,0)
        self.score.write(f"Game Over :(",False,align="center" ,font=('Courier',25,'bold'))
        screen = Screen()
        screen.exitonclick()