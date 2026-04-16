from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.update_level()


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
    
    def update_level(self):
        self.goto(0, 260)
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)
