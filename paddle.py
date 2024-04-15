from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(2, 0.5)
        self.pencolor("white")
        self.fillcolor("white")
        self.penup()
        self.goto(position)

    def rightup_move(self):
        new = self.ycor()+20
        self.goto(self.xcor(), new)

    def rightdown_move(self):
        new = self.ycor() - 20
        self.goto(self.xcor(), new)
    def leftup_move(self):
        new = self.ycor() + 20
        self.goto(self.xcor(), new)
    def leftdown_move(self):
        new = self.ycor() - 20
        self.goto(self.xcor(), new)


