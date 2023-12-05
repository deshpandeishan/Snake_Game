from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

python = Snake()

screen.listen()
screen.onkey(python.up, "Up")
screen.onkey(python.down, "Down")
screen.onkey(python.left, "Left")
screen.onkey(python.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    python.move()

screen.exitonclick()