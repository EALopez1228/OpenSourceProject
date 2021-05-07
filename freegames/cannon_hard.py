"""CANNON GAME:
Fire at the targets coming from the RHS by left clicking to prevent them from reaching the end!

DIFFICULTY: HARD

Modifications added: 
- Added difficulties to the game for more variation
- Added sound to signify a cannonball firing
- Added a background for a nicer aesthetic
- Added a Game Over Notification for when the user has lost
- Added sound when a Game Over is reached to further rub it in that you have lost
"""

#We import turtle and winsound to add sound effects and display
import turtle
import winsound
from random import randrange
from turtle import *
from freegames import vector


#We used 'bgpic' from the turtle library to change the background from white to a chosen gif
bgpic("star2.gif")
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

#Manages the sound effects, it is called when you fire the cannon
def play():
    winsound.Beep(500,50) 

#Plays a buzzer sound, called when the user has lost the game
def gameOver():
    winsound.PlaySound('buzzer_x.wav',winsound.SND_ASYNC)

#Handles what actions will be taken when the user taps the screen 

def tap(x, y):
    "Respond to screen tap."
    #If a ball is currently not inside the screen, spawns a new ball upon clicking
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25 #lowering the speed numerator makes the physics of the cannonball heavier
        speed.y = (y + 200) / 25 
        play()

#Function to test whether or not an object is inside the screen
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

#Function in charge of drawing and spawning new targets
def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'green') #20

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red') #6

    update()


#Function in charge of moving the targets along the map
def move():
    "Move ball and targets."

    #Handles the location at which targets will be spawned
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)


    #Handles move speed of targets
    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()


    #Handles when a target is hit
    for target in dupe:
        if abs(target - ball) > 13:
             targets.append(target)
             
             
            

    draw()

    #Tracks location of targets. If one has left the screen, a Game Over has been reached ending the game
    for target in targets:
        if not inside(target):
            color("yellow")
            write("GAME OVER",move = False, align = "right", font=("Arial", 20, 'bold'))
            gameOver()
            return

    #Controls the speed of the game, the lower the number the faster the speed of the game
    ontimer(move, 30) 

#Initializes the screen and Loops until a Game Over has been reached
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()