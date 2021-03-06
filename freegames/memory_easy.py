#creating an easy version of the memory game (4x4)
"""
Changes:
1. Changed 8x8 to 4x4
2. Added more images 
3. Randomized which image would appear at the end
4. Lowered numbers allowed in game
"""
from random import *
from turtle import *
from time import *
from sys import *
from freegames import path
import os

#This holds the value of the current working directory for easier file referencing
cwd = os.path.dirname(os.path.realpath(__file__))

#Creating the picture and tile objects
image_dic = {} #Making a random image to appear when doing puzzle
image_dic['car'] = path(cwd + '/car.gif')
image_dic['dino'] = path(cwd + '/dinosaur.gif')
image_dic['house'] = path(cwd + '/house.gif')
image_dic['dog'] = path(cwd + '/dog.gif')
image_dic['nova'] = path(cwd + '/supernova.gif')
image = choice(list(image_dic.values()))
tiles = list(range(8)) * 2
state = {'mark': None}
hide = [True] * 16

#Creating a square plus its size components
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(100)
        left(90)
    end_fill()

#Indexes of each tile (1-16)
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 100+ ((y + 200) // 100) * 4)

#How many tiles
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 4) * 100 - 200, (count // 4) * 100 - 200

#Lets the user tap on tiles and reveal numbers, and give error if out of scope of tiles
def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot #if you click somewhere outside the boxes get error
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

#Drawing the images and tiles
def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(image)
    stamp()

    for count in range(16):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']
#Out of bounds error
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)
#Shuffling of tile numbers and creating the viewer
shuffle(tiles)
setup(420, 420, 370, 0) #Setting the python viewer to middle top screen and ratio of 420,420
addshape(image) #Adding all the random images
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
