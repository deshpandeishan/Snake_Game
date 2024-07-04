from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.update_scores()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scores()

    def update_scores(self):
        self.write(f"Score: {self.score}", align='center', font=('Courier', 27, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Courier', 30, 'normal'))
