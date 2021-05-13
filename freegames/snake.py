"""Snake, classic arcade game.
"""

#Libraries we will be using for this program
#playsound manages the sounds being played
#turtle manages GUI and display
from playsound import playsound
from turtle import *
from random import randrange
from freegames import square, vector


#Globals to keep track of gamespeed, snake and food spawning
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
gamespeed = 50 #default snake speed

#Plays a buzzer sound, called when the user has lost the game
def gameOver():
    #winsound.PlaySound('buzzer_x.wav',winsound.SND_ASYNC)
    playsound('roblox.mp3', False)

#We used 'bgpic' from the turtle library to change the background from white to a chosen gif
bgpic("forest.gif")

#Change handles snake's direction.
def change(x, y):
    aim.x = x
    aim.y = y

#Function to test whether or not an object is inside the screen
def inside(head):
    "Return True if head inside boundaries."
    return -220 < head.x < 210 and -210 < head.y < 210

#Move handles the snakes constant progression forward as well as speed
def move():
    global gamespeed

    head = snake[-1].copy()
    head.move(aim)

    #If the snake has either gone out of bounds or collided with itself
    #we have reached a game over
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        gameOver()
        return

    snake.append(head)

    #If we have ran into a food object, increment the size of the snake
    # and speed up the snake
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        playsound("ping.wav", False)
        gamespeed -= 1
    else:
        snake.pop(0)

    clear()

    #Handles the creation of the target and snake objects
    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, gamespeed)


#Initializes the GUI and response to user inputs
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
