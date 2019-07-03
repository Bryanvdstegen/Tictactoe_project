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
bgimg = pygame.transform.scale(bgimg,(screenHeight, screenWidth)) # Centers picture

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

# Determine how to win
def gameWon(board):
    global grid, winner

    for x in range(0, 3):
        if ((grid[0][x] == grid[1][x] == grid[2][x]) and \
                (grid[0][x] is not None)):
            winner = grid[0][x]
            pygame.draw.line(board, (250, 0, 0), (0, (x + 1) * 100 - 50), \
                             (300, (x + 1) * 100 - 50), 2)
            break

    for y in range(0, 3):
        if (grid[y][0] == grid[y][1] == grid[y][2]) and \
                (grid[y][0] is not None):
            winner = grid[y][0]
            pygame.draw.line(board, (250, 0, 0), ((y + 1) * 100 - 50, 0), \
                             ((y + 1) * 100 - 50, 300), 2)
            break

    if (grid[0][0] == grid[1][1] == grid[2][2]) and \
            (grid[0][0] is not None):
        winner = grid[0][0]
        pygame.draw.line(board, (250, 0, 0), (50, 50), (250, 250), 2)

    if (grid[2][0] == grid[1][1] == grid[0][2]) and \
            (grid[0][2] is not None):
        winner = grid[0][2]
        pygame.draw.line(board, (250, 0, 0), (250, 50), (50, 250), 2)

# dumbAI - pick a random spot on the board
def dumbAI(board):
    global player, grid

    if (player == 1):
        print("computer")
        blanks = checkBlanks(grid)
        if len(blanks) > 0:
            move = random.choice(blanks)
            drawMove(board, move[0], move[1], player)
    player = -1

def evaluate(state):
    if wins(state, 1):
        score = 1
    elif wins(state, -1):
        score = -1
    else:
        score = 0
    return score

# how to win
def wins(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],

        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    return [player, player, player] in win_state

def minimax(state, depth, currPlayer):
    if currPlayer == 1:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in checkBlanks(state):
        x, y = cell[0], cell[1]
        state[x][y] = currPlayer
        score = minimax(state, depth - 1, currPlayer)
        state[x][y] = 0
        score[0], score[1] = x, y

        if currPlayer == 1:
            if score[2] > best[2]:
                #print("Score:")
                #print(score)
                #print("best:")
                #print(best)
                best = score # max value
                #print(best)
        else:
            if score[2] < best[2]:
                best = score # min value
    #print(best)
    return best

def game_over(state):
    return wins(state, -1) or wins(state, 1)

def checkBlanks(board):
    # should return an array of black cells
    blanks = []
    for index, row in enumerate(board):
        for index2, cell in enumerate(row):
            if cell == None:
                blanks.append([index, index2])
    return blanks

def main():
    pygame.init()
    ttt = pygame.display.set_mode([screenWidth, screenHeight])
    pygame.display.set_caption('Tic-Tac-Toe')

    global player
    board = initBoard(ttt)

    running = 1
    while (running == 1):
        for event in pygame.event.get():
            if event.type is QUIT:
              print("exit")
              running = 0
              pygame.display.quit()

            # ***** FOR DEMO: COMMENT THE TWO LINES BELOW WHEN PLAYING VERSUS COMPUTER *****
            elif event.type is MOUSEBUTTONDOWN:
              clickBoard(board)
            # ***** FOR DEMO: UNCOMMENT ALL BELOW WHEN PLAYING VERSUS COMPUTER *****
            elif event.type is MOUSEBUTTONDOWN and player == -1: 
               clickBoard(board)
            elif player == 1:
               dumbAI(board) #uncomment to implement dumbAI

            gameWon(board)

            showBoard(ttt, board)

if __name__ == "__main__":
    main()