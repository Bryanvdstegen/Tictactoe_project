# version 2.0 using pygame

# Set up and load pygame libraries
import pygame
from pygame import *
import random
from math import inf as infinity
import copy

# Set display
screenWidth = 300
consoleHeight = 25
screenHeight = screenWidth + consoleHeight

# Create the game board
backgroundColor = (0, 0, 0)
contentColor = (34, 166, 30)

# declare our global variables for the game
player = -1  # track whose turn it is; X goes first
grid = [[None, None, None],
        [None, None, None],
        [None, None, None]]

winner = None
bgimg = pygame.image.load('bgimg.png')

# initialize the board and return it as a variable
# ttt : a properly initialized pyGame display variable
# set up the background surface
# this function returns the value of the variable background (which is undefined).
def initBoard(ttt):
    background = pygame.Surface(ttt.get_size())
    background = background.convert()
    background.fill(backgroundColor)
    background.blit(bgimg, (0, 0))

    for num in range(2):
        pygame.draw.line(background, contentColor, (0, ((screenHeight - consoleHeight) / 3) * (num + 1)),
                         (screenWidth, ((screenHeight - consoleHeight) / 3) * (num + 1)), 2)

        pygame.draw.line(background, contentColor, (((screenWidth) / 3) * (num + 1), 0),
                         (((screenWidth) / 3) * (num + 1), (screenHeight - consoleHeight)), 2)

    return background # board is all black at this point
    ## credit to Christian for this 
(-------------------------------------------------------)
# Set up and load pygame libraries
import pygame
from pygame.locals import *

# Set display
pygame.init()
ttt = pygame.display.set_mode((300,325))
pygame.display.set_caption = ('Tic-Tac-Toe')

# Loop until user quits the game (x out of gameboard)

# create the game board
board = initBoard (ttt)

running = 1
while (running==1):
    for event in pygame.event.get():
        if event.type is QUIT:
            running = 0

def initBoard(ttt):

# initialize the board and return it as a variable
# ttt : a properly initialized pyGame display variable
# set up the background surface
# this function returns the value of the variable background (which is undefined).

    background = pygame.Surface (ttt.get_size())
    background = background.convert()
    background.fill ((250,250,250))
    ## credit to Christian for this 

    # draw grid lines

    # draw vertical lines
    pygame.draw.line (background, (0,0,0), (100,0), (100,300), 2) # background = surface variable, (000 = color, black), start and end points
    pygame.draw.line (background, (0,0,0), (200,0), (200,300), 2)

    # draw horizontal lines
    pygame.draw.line (background, (0,0,0), (0,100), (300,100), 2)
    pygame.draw.line (background, (0,0,0), (0,200), (300,200), 2)

    return background # board is all black at this point


    # Need a variable representing the display,
    # and a variable representing the screen surface
def showBoard (ttt, board):

    # (re)draw the game board (board) on the screen (ttt)
    ttt.blit (board, (0,0))
    pygame.display.flip()

while (running==1):
    for event in pygame.event.get():
        if event.type is QUIT:
            running = 0
            
        # update the display
        showBoard (ttt, board)

# Configuring mouse clicks
# X will go first...
XO = "X"

# declare an empty grid
grid =  [ [ None, None, None ],
          [ None, None, None ],
          [ None, None, None ] ]

while (running==1):

    for event in pygame.event.get():

        if event.type is QUIT:
            running = 0

        elif event.type is MOUSEBUTTONDOWN:
            clickBoard(board)

        #update the display
            showBoard (ttt, board)

def boardPos (mouseX, mouseY):
    # determine the row the user clicked
    if (mouseY < 100):
        row = 0

    elif (mouseY < 200):
        row = 1

    else:
        row = 2

    # determine the column the user clicked
    if (mouseX < 100):
        row = 0

    elif (mouseX < 200):
        row = 1

    else:
        row = 2

    #return the row & column
    return (row, col)

def clickBoard (board):
    # determine where the user clicked on the board and draw the X or O
    # tell Python that we want access to the global variables grid & XO

    global grid, XO

    (mouseX, mouseY) = pygame.mouse.get_pos()
    (row, col) = boardPos (mouseX, mouseY)

    # make sure this space isn't used
    if ((grid[row][col] == "X") or (grid[row][col] == "O")):

        # this space is in use
        return

    # draw an X or O
    drawMove (board, row, col, XO)

    # toggle XO to the other player's move
    if (XO == "X"):
        XO = "O"
    else:
        XO = "X"
