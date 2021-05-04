"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""

#We import turtle and winsound to add sound effects and display
import turtle
import winsound
from random import randrange
from turtle import *
from freegames import vector


#We used bgpic from the turtle library to change the background from white to a chosen gif
bgpic("star2.gif")
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

#Manages the sound effects, is called when you fire the cannon
def play():
    winsound.Beep(500,50) #PlaySound('baseball_hit.wav',winsound.SND_ASYNC)

#Plays a buzzer sound when the user has lost the game
def gameOver():
    winsound.PlaySound('buzzer_x.wav',winsound.SND_ASYNC)

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 250) / 25 #lowering the speed numerator makes the physics of the cannonball heavier
        speed.y = (y + 250) / 25 #200
        play()

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(30, 'green') #20

    if inside(ball):
        goto(ball.x, ball.y)
        dot(12, 'red') #6

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
        if abs(target - ball) > 17: #13
            targets.append(target)


    draw()

    for target in targets:
        if not inside(target):
            color("yellow")
            write("GAME OVER",move = False, align = "right", font=("Arial", 20, 'bold'))
            gameOver()
            return

    ontimer(move, 30) #50

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
