import pgzrun
import pygame
from random import randint
from time import time
WIDTH = 700
HEIGHT = 700

dots = []
lines = []
start_time = 0
end_time = 0

next_dot = 0

for dot in range(0, 10):
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
    for line in lines:
        screen.draw.line(line[0], line[1], (200,200,200))

def on_mouse_down(pos):
    global next_dot
    global lines
    global start_time
    global end_time

    if next_dot == 0:
        start_time = time()

    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot-1].pos, dots[next_dot].pos))
        next_dot = next_dot+1
    else:
        lines = []
        next_dot = 0

    if next_dot == 10:
        end_time = time()

        game_time = end_time - start_time
        print("game time:", int(game_time))
pgzrun.go()