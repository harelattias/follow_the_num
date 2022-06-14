import pgzrun
import pygame
from random import randint
from time import time

WIDTH = 700
HEIGHT = 700

game_over = False
game_time = 999

number_of_dots = 10

dots = []
lines = []
start_time = 0
end_time = 0
rl_is_the_hacker = False

next_dot = 0

for dot in range(0, number_of_dots):
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
        screen.draw.line(line[0], line[1], (200, 200, 200))

    global game_time

    if game_over:
        screen.fill("pink")
        screen.draw.text("total:" " " + str(int(game_time)) + " " "seconds", topleft=(HEIGHT / 3.3, WIDTH / 2.2), fontsize=60)


def update():
    global rl_is_the_hacker
    if keyboard.w:
        rl_is_the_hacker = True

    global start_time
    if keyboard.s:
        start_time = time()


def on_mouse_down(pos):
    global next_dot
    global lines
    global start_time
    global end_time
    global rl_is_the_hacker
    global game_over
    global game_time
    global number_of_dots

    if next_dot == 0:
        start_time = time()

    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot = next_dot + 1
    else:
        lines = []
        next_dot = 0

    if next_dot == number_of_dots:
        end_time = time()
        game_over = True

        if rl_is_the_hacker == False:
            game_time = end_time - start_time
        else:
            game_time = 1

        print("game time:", int(game_time))


pgzrun.go()