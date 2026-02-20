
import random
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
    "orange",
    "pink",
    "brown",
    "black",
    "cyan",
    "magenta",
    "lime",
    "navy",
    "gold",
    "coral"
]




def draw_shape(n):
    for _ in range(n):
        angle = 360 / n
        timmy.forward(100)
        timmy.right(angle)

for shape in range(3,11):
    timmy.color(random.choice(colors))
    draw_shape(shape)
        
#draw_shape(10)

screen.exitonclick()