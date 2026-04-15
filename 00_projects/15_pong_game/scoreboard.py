from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-50, 250)
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 250)
        self.write(":",align='center', font=('Arial', 28, 'bold'))
        self.goto(-50, 250)
        self.write(f"{self.l_score}",align='center', font=('Arial', 28, 'bold'))
        self.goto(50, 250)
        self.write(f"{self.r_score}",align='center', font=('Arial', 28, 'bold'))