from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(600, 600)
screen.title("Snake Game")
screen.bgcolor("black")


segments_list = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in segments_list:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    screen.tracer(0)
    segments.append(new_segment)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for segment_number in range(len(segments) - 1, 0, -1):
        x = segments[segment_number - 1].xcor()
        y = segments[segment_number - 1].ycor()
        segments[segment_number].goto(x, y)
    segments[0].fd(20)
    segments[0].lt(90)



screen.exitonclick()
