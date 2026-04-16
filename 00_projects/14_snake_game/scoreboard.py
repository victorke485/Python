from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        try:
            with open("00_projects/14_snake_game/data.txt") as file:
                self.high_score = int(file.read())
        except:
            print("An error occured. Intializing high score to be 0.")
            self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_score()
        
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("00_projects/14_snake_game/data.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"High Score: {self.high_score}      Score: {self.score}", align="center", font=("Arial", 24, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))