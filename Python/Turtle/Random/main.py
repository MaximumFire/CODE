from turtle import *
from random import *

t = Turtle()

while True:
    direction = randint(0, 3)
    t.speed(1000)
    if direction == 1:
        t.left(90)
    if direction == 2:
        t.right(90)
    if direction == 3:
        t.left(45)
    if direction == 0:
        t.right(45)
    t.forward(randint(10, 25))

