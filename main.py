import random

import colorgram
import turtle as t

def get_color_list():
    colors = colorgram.extract('image.jpeg',50)
    nl = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        nl.append((r,g,b))

    return nl


tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.setposition(-200, -200)
tim.speed(40)
for _ in range(10):
    tim.penup()
    tim.setposition(-200, tim.position()[1]+50)
    for _ in range(100):
        tim.dot(20,random.choice(get_color_list()))
        tim.penup()
        tim.forward(50)


screen = t.Screen()
screen.exitonclick()
