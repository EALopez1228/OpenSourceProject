# OpenSourceProject

CPSC254-OpenSourceProject
TEAM MEMBERS: Emilio Lopez, Francisco Bolanos, Zach Serna

PROGRAMMING LANGUAGE USED: Python


Purpose: Our goal was to take an already existing piece of open source code and modify it
to add additional features that would support the user experience. For our project we chose
to modify a collection of arcade games that were available on GitHub for all users to modify.
Our main objectives were to create a more simplified and streamlined experience for those that
simply wanted to play the games as well as add more variety to the games we found to be the most
entertaining. We did this by adding the following features:

ISSUES ENCOUNTERED:
A major struggle for us was simply learning a new language. Most of our group had little to no
experience with Python, so it took us some time to understand how the language worked exactly.
When modifying the cannon game, adding sound effects proved to be troublesome as properly
locating the sound was difficult with an overall lack of Python experience.

Some issues that were in the memory game was that it wasn't documented as well as it could have
been by the original creator. Due to this, when trying to modify the size for the 4x4 at first it
would have the tiles just in the lower left corner and the rest of the picture was shown
as if the rest of the tiles were uncovered. Plus when clicking on the 4x4 tiles in the lower
left corner not all of the numbers would appear correctly. Sometimes when clicking those tiles
the numbers would appear above the tile or somewhere else completely. This was thankfully resolved
when we were able to figure out how to alter two functions in the program.

DEPENDENCIES:
In order to run the program properly, you will need Tkinter, playsound, and Turtle which can be installed via the Python console.
These can be installed with a simple installation command: $ pip install (Program)

RUNNING THE PROGRAM:
To run the program, simply download the zip attached to the submission, install the dependencies, and use the command: $ python3 -m freegames.mainmenu

MODIFICATIONS:


MENU:
To make the games easier to access for the user, we added a menu. This allows the user to simply
press a button to select the game they desire to play as opposed to typing in console commands to
access the games.

CANNON:
We modified the cannon game to include several difficulties in the case where the original game proved
to be too easy or too hard. To add to the aesthetic of the game we have also added sound effects for
when the user fires off a cannonball as well as a sound effect for when a Game over is reached. A
Background was also added to the game as opposed to the default white background for a nicer overall
appearance.

MEMORY:
We modified the memory game from the original to include new difficulties, Easy and Hard. This is to
let younger kids have a go at the memory game while not making it a hard challenge. On the other side
the hard difficulty includes one hundred tiles for anyone who wants to experience a challenge. We also
included new images to appear once you complete the game. Originally the game only included one image,
a red car. However, now the both the memory games (Easy/Hard) have a total of five images:
car, dinosaur, house, dog, and supernova; they are picked at random. Therefore, the only way to know
what image you're going to get is by completing the game.

USE OF CASE TOOLS:
To help coordinate our work and divide effort evenly, we used GitHub to track our progress on the project
as well as update one another on our works so far.

GUI:
Adding a menu was our main choice of how to implement a GUI. We felt the menu would be much more accessible
to those with less experience coding and simply wanted to enjoy the games.

HIGH LEVEL LANGUAGE:
We chose to user Python for our programs.

COMMUNICATION WITH GROUP MEMBERS:
Using a combination of GitHub and Discord has allowed us to coordinate a lot even during the pandemic. We
were able to meet up over Discord calls and divide up the work evenly.

CONTRIBUTION TO BASE CODE:
See "Modifications" above

CODE DESIGN:
We added comments to the more difficult to understand portions of the code for clarity's sake as well as
any lines of code we personally added.
