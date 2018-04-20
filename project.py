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



# we are going to code the part of the game where we are moving the tetris pieces
# this code was created in reference to the "Tetris (Python Reacipe)" presented on ActiveState Code
left = 'left'
right = 'right'
turn = 'turn'
down = 'down'
quite = 'quit'

shaft = None

def turn_block(Blocks):
    result = []
    for x, y in block:
        result.append((y, -x))
    return result

def get_command(next_fall_time):
    while True: 
        timeout = next_fall_time - time.time()
        if timeout > 0.0:
            (r, w, e) = select.select([ sys.stdin ], [], [], timeout)
        else:
            raise Timeout()
        if sys.stdin not in r:
            raise Timeout()
        key = os.read(sys.stdin.fileno(), 1)
        elif key == 'Left':
            return left
        elif key == 'Right':
            return right
        elif key == 'Up':
            return turn
        elif key == 'Down':
            return down
        elif key == 'q':
            return quit
    #now we will take care of random buttons being pressed
        else: 
            pass
        
def place_block(Blocks, coordinates, color):
    global shaft, witdh, height
    Block_x, Block_y = coordinates
    for stone_x, stone_y in Block:
        x = Block_x + stone_x
        y = Block_y + stone_y
        if (x < 0 or x >= width or
            y < 0 or y >= height or
            shaft[y][x] != empty):
    for stone_x, stone_y in Block:
        x = Block_x + stone_x
        y = Block_y + stone_y
        shaft[y][x] = color
    return True



