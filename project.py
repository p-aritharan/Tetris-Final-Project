import pygame
from pygame.locals import *
import math
import random

Block1 = pygame.image.load("Tetris Final Project/Data/Tetris Blocks/Block1.gif")
Block2 = pygame.image.load("Tetris Final Project/Data/Tetris Blocks/L-Block.gif")
Block3 = pygame.image.load("Tetris Final Project/Data/Tetris Blocks/L-Block2.gif")
Block4 = pygame.image.load("Tetris Final Project/Data/Tetris Blocks/SquareBlock.gif")
Block5 = pygame.image.load("Tetris Final Project/Data/Tetris Blocks/StepBlock1.gif")
Block6 = pygame.image.load("Tetris Final Project/Data/Tetris Blocks/StepBlock2.gif")
Block7 = pygame.image.load("Tetris Final Project/Data/Tetris Blocks/T-Block.gif")

def startgame():

pygame.init()
width, height = 500, 750
screen = pygame.display.set_mode((width, height))
#finally got the background to load
sky = pygame.image.load("Tetris Final Project/Data/Background/sky.gif")
timer = 0

running = 1
done = 0

# from random import randint
# rblock = randint(1,7)

# if rblock == 1:
#     pygame.display.update(screen.blit(Block1))
# if rblock == 2:
#     pygame.display.update(screen.blit(Block2))
# if rblock == 3:
#     pygame.display.update(screen.blit(Block3))
# if rblock == 4:
#     pygame.display.update(screen.blit(Block4))
# if rblock == 5:
#     pygame.display.update(screen.blit(Block5))
# if rblock == 6:
#     pygame.display.update(screen.blit(Block6))
# if rblock == 7:
#     pygame.display.update(screen.blit(Block7))


while running:
    timer-=1

    screen.fill(0)

    for x in range(width//sky.get_width()+1):
        for y in range(height//sky.get_height()+1):
             pygame.display.update(screen.blit(sky,(x*100,y*100)))
    
    startgame()


    # if timer==0:
    #     rblock.append([640, random.randint(50,430)])
    #     timer=100-(timer*2)
    #     if timer1>=35:
    #         timer1=35
    #     else:
    #         timer1+=5
    # index=0
    # for badguy in rblock:
    #     if badguy[0]<-64:
    #         rblock.pop(index)
    #     badguy[0]-=7


#4/12 just got github as well as collaboration working

