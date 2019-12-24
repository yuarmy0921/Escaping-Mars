import pygame
import os, sys

def load_image(name, prev, colorkey = None):
    '''
    把圖片載下來
    '''
    fullname = os.path.join('game_material/'+prev+"/", name)
    try:
        #pygame.image.load(圖片檔案路徑)
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image: ', name)
        raise SystemExit(message)
    #把圖片轉換成最適合呈現的樣子
    image = image.convert()
    if colorkey is not True:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    #get_rect():把rect設定成圖片大小
    return image, image.get_rect()

class MazeBarrier(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.image, self.rect = load_image("barrier.png", "main_pic")

    def fire(self):
        # 每一個障礙物都會燒起來！
        # 原本的狀態先存起來，火燒完後再回來
        ori_image, ori_rect = self.image, self.rect
        self.image, self.rect = load_image("","main_pic")
        time.sleep(0.5)
        self.image, self.rect = ori_image, ori_rect

# 遊戲最最初始值設定，主程式一定是要先跑這個，阿然後可能還要再call NPC and BTS
class MazeGame:

    def __init__(self):
        self.unit = 10

        # The following attributes will be initialized later
        self.maze = None
        self.barriers = []
        self.exit_point = None
        #self.NPC = NPC()
        #self.BTS = BTS()

        self.ground = load_image("mars.jpg", "main_pic")
       
        # Build Maze
        with open(("maze.txt"), "r") as f:
            # Reserve space for maze
            lines = f.read().strip("\n"),split("\n") # Read the map
            maze = np.zeros(len(lines)*unit, len(lines[0])*unit, 3) # (height, width, depth)

            # Initialize maze row by row
            for row, line in enumerate(lines):
                for col, symbol in enumerate(line):
                    if symbol == '0': # 障礙物
                        # Create barrier
                        barrier = MazeBarrier((col*unit, row*unit))
                        self.barriers.append(barrier)
                    elif symbol == '1': # 路，不需要load image，用背景即可
                        pass
                    elif symbol == 'S': # 起點，call player_class
                        # 有要set color 嗎？沒有就pass下面那個
                        maze[row*unit:row*unit+unit, col*unit:col*unit+unit, 0] = 255

                        # Create player
                        #self.player = Player((col*unit, row*unit))
                        # 我想要做的是，這是在傳player位置，安捏干丟？？？？
                    elif symbol == 'F': # 終點
                        # 設成紅色
                        maze[row*unit:row*unit+unit, col*unit:col*uit+unit, 0] = 255

                        # Record the exit point
                        self.exit_point = (col*unit, row*unit)
                    else:
                        raise Exception("Invalid symbol in maze '%s'" % symbol)

        # Create groups
        self.barrier_group = pygame.sprite.Group(self.barriers)

game = MazeGame()
