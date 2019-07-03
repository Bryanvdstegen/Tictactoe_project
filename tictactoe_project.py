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


def drawStatus(board):
    global player, winner

    if player == -1:
      play = "X"
    else:
      play = "O"

    if (winner is None):
      message = play + "'s turn"
    else:
      if(winner == -1):
        message = "X won!"
      else:
        message = "O won!"

    font = pygame.font.Font(None, consoleHeight)
    text = font.render(message, 1, contentColor)

    board.fill(backgroundColor, (0, screenHeight - consoleHeight, screenWidth, consoleHeight))
    board.blit(bgimg, (0, screenHeight - consoleHeight))
    board.blit(text, ((screenWidth - text.get_width()) / 2, screenHeight - consoleHeight))

# Need a variable representing the display,
# and a variable representing the screen surface
def showBoard(ttt, board):
    drawStatus(board)
    ttt.blit(board, (0, 0))
    pygame.display.flip()

# (re)draw the game board (board) on the screen
def clickBoard(board):
    global grid, player

    (mouseX, mouseY) = pygame.mouse.get_pos()
    (x, y) = boardPos(mouseX, mouseY)

    if ((grid[x][y] == -1) or (grid[x][y] == 1)):
        return

    drawMove(board, x, y, player)

    if (player == -1):
        player = 1
    else:
        player = -1

def drawMove(board, boardRow, boardCol, Piece):
    centerX = ((boardRow) * (screenWidth / 3)) + 25
    centerY = ((boardCol) * ((screenHeight - consoleHeight) / 3)) + 20

    font = pygame.font.Font(None, int((screenWidth / 3)))

    if (Piece == 1):
        text = font.render("O", 1, contentColor)
        board.blit(text, (int(centerX), int(centerY)))
    else:
        text = font.render("X", 1, contentColor)
        board.blit(text, (int(centerX), int(centerY)))

    grid[boardRow][boardCol] = Piece
    # print(str(boardRow) + "_" + str(boardCol) + "_pience: "+ str(Piece))

# Configuring mouse clicks
# Determine where the user clicked on the board and draw the X or O
def boardPos(mouseX, mouseY):
    print(mouseY)
    if (mouseY < 100):
        y = 0
        #print(x)
    elif (mouseY < 200):
        y = 1
        #print(x)
    else:
        y = 2
        #print(x)

    print(mouseX)
    if (mouseX < 100):
        x = 0
        #print(y)
    elif (mouseX < 200):
        x = 1
        #print(y)
    else:
        x = 2
        #print(y)

    return (x, y)
(-----------------------------)
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
