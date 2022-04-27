import pgzrun
import pygame
from random import randint

WIDTH = 700
HEIGHT = 700

dots = []
lines = []

next_dot = 0

for dot in range(0,10):
    actor = Actor("dot")
    actor.pos = randint(70, (WIDTH - 70)), \
    randint(70, (HEIGHT - 70))
    dots.append(actor)

def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number = number + 1
pgzrun.go()