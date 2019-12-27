import pygame, os, sys
import cv2
import numpy as np
from pygame.locals import *

class MazeBarrier(pygame.sprite.Sprite):

    def __init__(self, position, row, col, unit, maze, x,y): # position是傳進行與列
        super().__init__()
        barrier_image = cv2.imread("./game_material/main_pic/barrier.png")
        barrier_image = cv2.resize(barrier_image, (unit, unit))
        barrier_image = cv2.cvtColor(barrier_image, cv2.COLOR_BGR2RGB)
        maze[x*2+row*unit:x*2+row*unit+unit, y+col*unit:y+col*unit+unit, :] = barrier_image
        self.image = pygame.surfarray.make_surface(np.transpose(barrier_image ,(1,0,2)))
        self.rect = pygame.Rect(position, barrier_image.shape[:2])

class Maze(pygame.sprite.Sprite):

    def __init__(self, position, texture):
        super().__init__()
        self.texture = texture
        self.image = pygame.surfarray.make_surface(np.transpose(texture, (1,0,2)))
        self.rect = pygame.Rect(position,self.texture.shape[:2])

class MazeGame:

    def __init__(self):
        unit = 15
        width, height = 1440, 800
        maze_width, maze_height = 1140, 650

        # The following attributes will be initialized later
        self.maze = None
        self.barriers = []
        self.exit_point = None
        #self.NPC = NPC()
        #self.BTS = BTS()
       
        # Build Maze
        with open(("maze.txt"), "r") as f:
            # Reserve space for maze
            lines = f.read().strip("\n").split("\n") # Read the map
            maze = np.zeros((height, width, 3))
            # numpy shape (height, width, depth)
            # cv2.resize(image,(width, height))
            # [height, width,:]

            # resize bg
            bg = cv2.imread("./game_material/main_pic/mars.jpg")
            bg = cv2.cvtColor(bg, cv2.COLOR_BGR2RGB)
            bg = cv2.resize(bg, (maze_width, maze_height))
            x, y = (height - maze_height)//2, (width - maze_width)//2
            maze[x*2:x*2+maze_height, y:y+maze_width, :] = bg
            # 左上角：(150, 75)

            # Initialize maze row by row
            for row, line in enumerate(lines):
                for col, symbol in enumerate(line):
                    if symbol == '0': # 障礙物
                        # Create barrier
                        barrier = MazeBarrier((col*unit, row*unit),row,col,unit,maze,x,y)
                        self.barriers.append(barrier)
                    elif symbol == '1': # 路，不需要load image，用背景即可
                        pass
                    elif symbol == 'S': # 起點
                        # 設成red
                        maze[x*2+row*unit:x*2+row*unit+unit, y+col*unit:y+col*unit+unit, 1] = 255

                        # Create player
                        #self.player = Player((col*unit, row*unit))
                        # 我想要做的是，這是在傳player位置，安捏干丟？？？？
                    elif symbol == 'F': # 終點
                        # 設成red
                        maze[x*2+row*unit:x*2+row*unit+unit, y+col*unit:y+col*unit+unit, 2] = 255

                        # Record the exit point
                        self.exit_point = (col*unit, row*unit)
                    else:
                        raise Exception("Invalid symbol in maze '%s'" % symbol)
        # Save maze
        self.maze = Maze((0,0), maze.copy())
        
        # Create groups
        self.barrier_group = pygame.sprite.Group(self.barriers)

def main():
    pygame.init()
    game = MazeGame()
    screen = pygame.display.set_mode((game.maze.image.get_size()))
    screen.blit(game.maze.image, game.maze.rect)
    quit_flag = False
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                quit_flag = True
        if quit_flag:
            break
    pygame.quit()

main()

"""
問題
1. 為什麼是藍色系XD
2. height and width 在nparray跟cv2再畫上去的不同，搞不清楚
3. could not broadcast input array from shape (15,15,3) into shape (30,15,3)
   這個是發生什麼事，在line_12
   調位置整個都不太懂
"""

# load numpy abd cv2
# initialize maze
# load image , iamread("檔案路徑")
# resize image
# assign resized image to 正確的 位置

