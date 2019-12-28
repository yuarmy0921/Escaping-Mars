import pygame, cv2
import numpy as np

class MazeGame:

    def __init__(self):
        unit = 15
        width, height = 1440, 800
        maze_width, maze_height = 1440, 650
        screen = pygame.display.set_mode((1440, 800))

        # The following attributes will be initialized later
        self.maze = None
        self.barriers = []
        self.exit_point = None
        #self.NPC = NPC()
        #self.BTS = BTS()
       
        # Build Maze
        with open(("maze(revised).txt"), "r") as f:
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
            print(x, y)
            maze[x*2:x*2+maze_height, y:y+maze_width, :] = bg
            bg = pygame.surfarray.make_surface(np.transpose(bg, (1,0,2)))
            # 左上角：(150, 75)
            screen.blit(bg, (y,x))

def main():
    pygame.init()
    game = MazeGame()
    quit_flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                quit_flag = True
        if quit_flag:
            break
    pygame.quit()

main()