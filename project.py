import pygame
from pygame.locals import *
import math
import random

Block1 = pygame.image.load("Block1.png")
Block2 = pygame.image.load("L-Block.gif")
Block3 = pygame.image.load("L-Block2.gif")
Block4 = pygame.image.load("SquareBlock.gif")
Block5 = pygame.image.load("StepBlock1.gif")
Block6 = pygame.image.load("StepBlock2.gif")
Block7 = pygame.image.load("T-Block.gif")
sky = pygame.image.load("sky.gif")
BLOCKS = [Block1, Block2, Block3, Block4, Block5, Block6, Block7]

def startgame():
    pygame.init()
    width, height = 500, 500
    screen = pygame.display.set_mode((width, height))
#finally got the background to load
    timer = 0

    running = 1
    done = 0

    while running:
        timer-=1

        screen.fill(0)

        for x in range(width//sky.get_width()+1):
            for y in range(height//sky.get_height()+1):
             pygame.display.update(screen.blit(sky,(x*100,y*100)))
    
    
startgame()

#4/12 just got github as well as collaboration working


