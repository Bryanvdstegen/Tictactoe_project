# version 2.0 using pygame

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