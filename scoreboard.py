from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
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
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Courier', 27, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scores()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Courier', 30, 'normal'))
