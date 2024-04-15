from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.second_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):

        self.goto(100, 150)

        self.write(f"{self.score}", align='left', font=('Arial', 24, 'normal'))

        self.goto(-100, 150)

        self.write(f"{self.second_score}", align='right', font=('Arial', 24, 'normal'))

    def right_player(self):
        self.clear()
        self.second_score += 1
        self.update_scoreboard()
    def left_player(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()




