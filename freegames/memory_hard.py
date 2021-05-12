# Hard version of memory game (10x10)
"""
Changes:
1. Changed 8x8 to 10x10
2. Added more images 
3. Randomized which image would appear at the end
4. Raised numbers allowed in game
5. Changed font size to not overstep on other tiles
"""

from random import *
from turtle import *
from time import *
from sys import *
from freegames import path

#Creating the picture and tile objects
image_dic = {} #Making a random image to appear when doing puzzle
image_dic['car'] = path('car.gif')
image_dic['dino'] = path('dinosaur.gif')
image_dic['house'] = path('house.gif')
image_dic['dog'] = path('dog.gif')
image_dic['nova'] = path('supernova.gif')
image = choice(list(image_dic.values()))
tiles = list(range(50)) * 2
state = {'mark': None}
hide = [True] * 100

#Creating a square plus its size components
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(80)
        left(90)
    end_fill()

#Indexes of each tile (1-100)
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 40 + ((y + 200) // 40) * 10)

#How many tiles
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 10) * 40 - 200, (count // 10) * 40 - 200

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

    for count in range(100):
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
        write(tiles[mark], font=('Arial', 22, 'normal'))

    update()
    ontimer(draw, 100)
#Shuffling of tile numbers and creating the viewer
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(image)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
