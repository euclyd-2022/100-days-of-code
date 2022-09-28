from turtle import Turtle
X_LOCATION = -270
Y_LOCATION = 270
FONT = ('Courier', 16, 'bold')
class Scoreboard(Turtle):

    def __init__(self):
        with open("data.txt") as file:
            high_score = file.read()
        self.score = 0
        self.highscore = int(high_score)
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(X_LOCATION, Y_LOCATION)
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()


    #def game_over(self):
     #   self.goto(0,0)
      #  self.write("GAME OVER", move=False, align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align="left", font=FONT)

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()


