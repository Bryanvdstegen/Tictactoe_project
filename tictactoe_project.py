# version 2.0 using pygame

# Set up and load pygame libraries
import pygame
from pygame.locals import *

# Set display
pygame.init()
ttt = pygame.display.set_mode((300,325))
pygame.display.set_caption = ('Tic-Tac-Toe')


# Loop until user quits the game

running = 1
while (running==1):
    for event in pygame.event.get():
        if event.type is QUIT:
            running = 0
