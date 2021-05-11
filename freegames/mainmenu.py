from freegames import square, vector, floor
from turtle import *
import os

tiles = [
    [-1050, 150],
    [-750, 150],
    [-450, 150],
    [-150, 150],
    [150, 150],
    [450, 150],
    [750, 150],
    [-1050, -150],
    [-750, -150],
    [-450, -150],
    [-150, -150],
    [150, -150],
    [450, -150],
    [750, -150],
    [-1050, -450],
    [-750, -450],
    [-450, -450],
    [-150, -450],
    [150, -450],
    [450, -450],
    [750, -450]
]

games = [
    "Ant",
    "Bagels",
    "Bounce",
    "Cannon",
    "Connect",
    "Crypto",
    "Fidget",
    "Flappy",
    "Guess",
    "Life",
    "Maze",
    "Memory",
    "Minesweep",
    "Pacman",
    "Pain",
    "Pong",
    "Simon",
    "Snake",
    "TicTacToe",
    "Tiles",
    "Tron"
]

def checkBox(clicked):
    index = 0;
    for i in tiles:
        if ((clicked[0] > i[0]) and (clicked[0] < i[0] + 300) and (clicked[1] > i[1]) and (clicked[1] < i[1] + 300)):
            return index

        index = index + 1

def RunGame(boxClicked):
    cwd = os.path.dirname(os.path.realpath(__file__))

    if(boxClicked == 0):
        os.system('python3 ' + cwd + '/ant.py')
    elif(boxClicked == 1):
        os.system('python3 ' + cwd + '/bagels.py')
    elif(boxClicked == 2):
        os.system('python3 ' + cwd + '/bounce.py')
    elif(boxClicked == 3):
        os.system('python3 ' + cwd + '/cannon.py')
    elif(boxClicked == 4):
        os.system('python3 ' + cwd + '/connect.py')
    elif(boxClicked == 5):
        os.system('python3 ' + cwd + '/crypto.py')
    elif(boxClicked == 6):
        os.system('python3 ' + cwd + '/fidget.py')
    elif(boxClicked == 7):
        os.system('python3 ' + cwd + '/flappy.py')
    elif(boxClicked == 8):
        os.system('python3 ' + cwd + '/guess.py')
    elif(boxClicked == 9):
        os.system('python3 ' + cwd + '/life.py')
    elif(boxClicked == 10):
        os.system('python3 ' + cwd + '/maze.py')
    elif(boxClicked == 11):
        os.system('python3 ' + cwd + '/memory.py')
    elif(boxClicked == 12):
        os.system('python3 ' + cwd + '/minesweeper.py')
    elif(boxClicked == 13):
        os.system('python3 ' + cwd + '/pacman.py')
    elif(boxClicked == 14):
        os.system('python3 ' + cwd + '/paint.py')
    elif(boxClicked == 15):
        os.system('python3 ' + cwd + '/pong.py')
    elif(boxClicked == 16):
        os.system('python3 ' + cwd + '/simonsays.py')
    elif(boxClicked == 17):
        os.system('python3 ' + cwd + '/snake.py')
    elif(boxClicked == 18):
        os.system('python3 ' + cwd + '/tictactoe.py')
    elif(boxClicked == 19):
        os.system('python3 ' + cwd + '/tiles.py')
    elif(boxClicked == 20):
        os.system('python3 ' + cwd + '/tron.py')


def grid():
    square(-1050, 150, 300, 'red')
    square(-750, 150, 300, 'blue')
    square(-450, 150, 300, 'red')
    square(-150, 150, 300, 'blue')
    square(150, 150, 300, 'red')
    square(450, 150, 300, 'blue')
    square(750, 150, 300, 'red')
    square(-1050, -150, 300, 'blue')
    square(-750, -150, 300, 'red')
    square(-450, -150, 300, 'blue')
    square(-150, -150, 300, 'red')
    square(150, -150, 300, 'blue')
    square(450, -150, 300, 'red')
    square(750, -150, 300, 'blue')
    square(-1050, -450, 300, 'red')
    square(-750, -450, 300, 'blue')
    square(-450, -450, 300, 'red')
    square(-150, -450, 300, 'blue')
    square(150, -450, 300, 'red')
    square(450, -450, 300, 'blue')
    square(750, -450, 300, 'red')

def draw():
    color('black')
    for i, j in zip(tiles, games):
        goto(i[0], i[1] + 150)
        text = j
        write(text, font=("Terminal", 40, 'normal'))


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


setup(2100,900, 370, 0)
hideturtle()
tracer(False)
grid()
draw()
onscreenclick(start)
done()
