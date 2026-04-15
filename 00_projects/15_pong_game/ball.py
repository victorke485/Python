from turtle import Turtle

class Ball(Turtle):

    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.2

    def move(self):
        y_cor = self.ycor() + self.y_move
        x_cor = self.xcor() + self.x_move      
        self.goto(x_cor, y_cor)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed * 0.5

    def reset_position(self):
        self.goto(0, 0)
        self.x_bounce()
        self.move_speed = 0.4
    