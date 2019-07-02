# version 2.0 using pygame

# Set up and load pygame libraries
import pygame
from pygame.locals import *

# Set display
pygame.init()
ttt = pygame.display.set_mode((300,325))
pygame.display.set_caption = ('Tic-Tac-Toe')

screenWidth = 300
consoleHeight = 25
screenHeight = screenWidth + consoleHeight

# Loop until user quits the game

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

    return background # is all back at this point

