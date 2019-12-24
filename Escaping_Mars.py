#建立遊戲素材
import pygame
import random 
import math
import os, sys
import time
from pygame.locals import *
from pygame.compat import geterror
#pygame.image.load()預設得到的type是surface
#pygame.sprite.Group.update：call the update method
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

def load_sound(name):
    #如果沒有成功載入音樂就不撥放
    class NoneSound:
        def play(self): pass
    #pygame.mixer：撥放音樂的module
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('game_material/voice/', name)
    print(fullname)
    try:
        #create a new sound object
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print('Cannot load a sound: ', name)
        raise SystemExit(message)
    return sound


#玩家
class Player(pygame.sprite.Sprite):
    '''
    隨著滑鼠移動，滑鼠要換成圖片!!!!!!
    碰到迷宮邊界則損血
    碰到NPC回血
    不會呼叫外面的參數
    只有玩家用pos，其他都用x y
    rect吃四個參數(左上角x座標, 左上角y座標, 長, 寬)
    '''
    def __init__(self, draw = screen):
        pygame.sprite.Sprite.__init__(self)
        screen = draw
        self.dead = False
        #被取代成滑鼠的圖片，已經convert完了
        self.image, self.rect = load_image()
        #把圖片轉成可以快速貼到螢幕上的形式
        self.image = self.image.convert_alpha()
        self.size = (self.rect.[2]//2, self.rect.[3]//2)
        pygame.mouse.set_visible(False)
        #初始位置
        self.pos = "自己設定!!!!!!!!!!!!!!!!!!!!!!!!!"
        self.last_pos = None
        pygame.mouse.set_pos([x, y])
        self.rect[0], self.rect[1] = self.pos[0]-self.size[0], self.pos[1]-self.size[1]
        self.draw(screen)


        #設定玩家血量，然後顯示血條：調整到難易適中，還要再回來設定!!!!!!!!!
        self.blood = 150
        #長150寬20
        self.blood_surface = pygame.Surface((self.blood, 20))
        self.blood_surface.fill((255,0,0))
        self.empty_surface = pygame.Surface((150, 20))
        self.empty_surface.fill((255, 255, 255))
        screen.blits(((self.empty_surface, (500, 150))), (self.blood_surface, (500, 150))))
        #然後玩家的初始設定大概差不多就結束了
        self.scream = load_sound("scream.wav")

    def walk(Self):
        self.pos = pygame.mouse.get_pos()
        self.rect[0], self.rect[1] = self.pos[0]-self.size[0], self.pos[1]-self.size[1]
        self.rect.move_ip(self.rect[0], self.rect[1])

    def stepback(self):
        Hua.move_ip(self.last_pos[0], self.last_pos[1])

    def recover(self):
        if self.blood <= 140:
            self.blood += 10
            self.blood_surface = pygame.Surface((self.blood, 20))
            self.blood_surface.fill((255,0,0))
            screen.blits(((empty_surface, (500, 150)), (blood_surface, (500, 150))))
        else:
            self.blood = 150
            self.blood_surface = pygame.Surface((self.blood, 20))
            self.blood_surface.fill((255,0,0))
            screen.blits(((empty_surface, (500, 150)), (blood_surface, (500, 150))))


    def injure(self, times, play):
        '''
        這裡完成了!!!!!!!!!!!!!!!!!!!!!!!!!!!
        '''
        if play:
            self.scream.play()
        #血條減少(一次把兩個surface貼上去)
        #這裡要調整難度!!!!!!!!!!!!!!!!!現在可以被摸15次
        for round in range(times):
            self.blood -= 10
            if self.blood > 0:
                self.blood_surface = pygame.Surface((self.blood, 20))
                self.blood_surface.fill((255,0,0))
                screen.blits(((empty_surface, (500, 150)), (blood_surface, (500, 150))))
            else:
                self.dead = True


    def update(self):
        #玩家狀態
        
        self.pos = pygame.mouse.get_pos()
        #這裡是在幹嘛???????????????
        self.rect.mid = pos


    
class BTS(pygame.sprite.Sprite):
    '''
    不用管分別的技能是甚麼，反正只要碰到就損血，另外寫碰到玩家時的行為
    設定進行速度
    把外界參數抓進來用(判斷碰撞)
    移動模式可能要改一下(不是隨機移動，不然會像撞球，從哪邊碰到障礙物也很難判斷)
    '''
    
    def __init__(self, draw = screen):
        pygame.sprite.Sprite.__init__(self)
        screen = draw
        self.image, self.rect = None, None
        self.x, self.y = None, None
        self.last_pos = None
        self.rect[0], self.rect[1] = self.pos[0], self.pos[1]
        self.draw(screen)
        self.skill = None 
        self.dx, self.dy = None, None

    def stepback(self):
        self.move_ip(self.last_pos[0], self.last_pos[1])

    def change_dir():    
        direction = random.randint(0, 360)
        radian = math.radians(direction)
        self.dx = speed*math.cos(radian)
        self.dy = speed*math.sin(radian)

    def walk(x = self.x, y = self.y, dx = self.dx, dy = self.dy):
        self.x += self.dx
        self.y += self.dy
        self.rect.move_ip(self.x, self.y)
        
    def update(self):
        self.walk()



class NPC(pygame.sprite.Sprite):
    '''
    技能都一樣，差別在於對話框不同
    遇到邊界要後退
    遇到玩家或NPC不能疊上去
    '''
    def __init__(self, draw = screen):
        pygame.sprite.Sprite.__init__(self)
        screen = draw
        self.image, self.rect = load_image()
        self.size = (self.rect[2], self.rect[3])
        self.x, self.y = None, None
        speed = 3
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.prev = None

        self.healing = None
        self.healflag = False
        #對話內容
        talk_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 10)
        self.alltalk = None
        
    def Up(self):
        self.prev = self.up
        self.y += speed
        self.rect.move_ip(self.x, self.y)
    def Down(self):
        self.prev = self.down
        self.y -= speed
        self.rect.move_ip(self.x, self.y)
    def Left(self):
        self.prev = self.left
        self.x -= speed
        self.rect.move_ip(self.x, self.y)
    def Right(self):
        self.prev = self.right
        self.x += speed
        self.rect.move_ip(self.x, self.y)

    def stepback(self):    
        '''
        碰到障礙物
        已經寫好啦!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        '''
        if self.prev == self.up:
            self.y -= speed
            self.rect.move_ip(self.x, self.y)
        elif self.prev == self.down:
            self.y += speed
            self.rect.move_ip(self.x, self.y)
        elif self.prev == self.left:
            self.x += speed
            self.rect.move_ip(self.x, self.y)
        elif self.prev == self.right:
            self.x -= speed
            self.rect.move_ip(self.x, self.y)
        else:
            pass
    
'''
    def trash_talk(self):
        
        碰到玩家
        講一些幹話
        
        class Talk(pygame.sprite.Sprite):
            def __init__(self, talk):
                pygame.sprite.Sprite.__init__(self)
                #從一群對話中隨機選出一句，對話放頭上(名字以上)，決定適當的距離!!!!!!!!!!
                self.talk = talk
                #convert()：建立副本
                self.talk = self.talk.convert()
                #文字框根據對話的長度來決定
                self.talk_bg = pygame.Surface((self.talk.get_width(), self.talk.get_height()))
                self.talk_bg.fill((255, 255, 255))
                self.talk_bg = self.talk_bg.convert()
                self.talk_bg.blit(self.talk, (0, 0))
                self.image, self.rect = self.talk_bg, 
        #建立計時器，維持幾秒
        #先這樣!!!!!!!!!!!!!!!!!!
        random_talk = self.alltalk[random.randint(0, len(self.alltalk)-1)]
        random_talk = pygame.sprite.GroupSingle(Talk(random_talk))
        screen.blit((random_talk.talk_bg, (self.x, self.y + 10)))
        pygame.time.wait(5000)
        #移除對話
'''

class MazeBarrier(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()
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
        self.Player = Player()
        self.NPC = NPC()
        self.BTS = BTS()

        self.ground = load_image("mars.jpg", "main_pic")
       
        # Build Maze
        with open("maze.txt"), "r") as f:
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
                        self.player = Player((col*unit, row*unit))
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
