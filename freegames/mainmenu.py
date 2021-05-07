from freegames import square, vector, floor
from turtle import *
import os

tiles = [
    [-600, 300],
    [-300, 300],
    [0, 300],
    [300, 300],
    [-600, 0],
    [-300, 0],
    [0, 0],
    [300, 0],
    [-600, -300],
    [-300, -300],
    [0, -300],
    [300, -300],
    [-600, -600],
    [-300, -600],
    [0, -600],
    [300, -600]
]

def checkBox(clicked):
    index = 0;
    for i in tiles:
        if ((clicked[0] > i[0]) and (clicked[0] < i[0] + 300) and (clicked[1] > i[1]) and (clicked[1] < i[1] + 300)):
            return index

        index = index + 1

def RunGame(boxClicked):

    if(boxClicked == 0):
        os.system("ant.py")
    elif(boxClicked == 1):
        os.system("bagels.py")
    elif(boxClicked == 2):
        os.system("bounce.py")
    elif(boxClicked == 3):
        os.system("cannon.py")
    elif(boxClicked == 4):
        os.system("connect.py")
    elif(boxClicked == 5):
        os.system("crypto.py")
    elif(boxClicked == 6):
        os.system("fidget.py")
    elif(boxClicked == 7):
        os.system("flappy.py")
    elif(boxClicked == 8):
        os.system("guess.py")
    elif(boxClicked == 9):
        os.system("life.py")
    elif(boxClicked == 10):
        os.system("maze.py")
    elif(boxClicked == 11):
        os.system("memory.py")
    elif(boxClicked == 12):
        os.system("minesweeper.py")
    elif(boxClicked == 13):
        os.system("pacman.py")
    elif(boxClicked == 14):
        os.system("paint.py")
    elif(boxClicked == 15):
        os.system("pong.py")


def grid():
    square(-600, 300, 300, 'red')
    square(-300, 300, 300, 'green')
    square(0, 300, 300, 'blue')
    square(300, 300, 300, 'purple')
    square(-600, 0, 300, 'green')
    square(-300, 0, 300, 'red')
    square(0, 0, 300, 'purple')
    square(300, 0, 300, 'blue')
    square(-600, -300, 300, 'blue')
    square(-300, -300, 300, 'purple')
    square(0, -300, 300, 'red')
    square(300, -300, 300, 'green')
    square(-600, -600, 300, 'purple')
    square(-300, -600, 300, 'blue')
    square(0, -600, 300, 'green')
    square(300, -600, 300, 'red')

def tap(x, y):
    "Respond to screen tap."
    onscreenclick(None)

    clicked = [x,y]

    boxClicked = checkBox(clicked)

    RunGame(boxClicked)

    onscreenclick(tap)

def start(x, y):
    "Start game."
    onscreenclick(tap)


setup(1200,1200, 370, 0)
hideturtle()
tracer(False)
grid()
onscreenclick(start)
done()
