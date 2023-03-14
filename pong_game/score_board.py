from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        self.clear()
        self.middle_line()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    def left_points_increase(self):
        self.right_score += 1
        self.update()

    def right_points_increase(self):
        self.left_score += 1
        self.update()

    def middle_line(self):
        self.pencolor("white")
        self.goto(0, 300)
        self.setheading(270)
        while self.ycor() > -300:
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)