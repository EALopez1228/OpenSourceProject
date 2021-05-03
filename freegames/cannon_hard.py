"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""
import turtle
import winsound
from random import randrange
from turtle import *
from freegames import vector

bgcolor("black")
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def play():
    winsound.Beep(500,50) #PlaySound('baseball_hit.wav',winsound.SND_ASYNC)


def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25 #200
        speed.y = (y + 200) / 25 #200
        play()

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue') #20

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red') #6

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
             targets.append(target)
             #play()
             
            

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 30) #50

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()