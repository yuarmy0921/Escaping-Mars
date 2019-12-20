#建立遊戲素材
import pygame
import random 
import math
import os, sys
from pygame.locals import *
from pygame.compat import geterror
#把collide設成一種event!!!!!!!
#載入遊戲：還要再回來檢查
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
    #這邊是在幹嘛?
    #colorkey：透明色鍵
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
    sprite的rect???????????
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.dead = False
        #被取代成滑鼠的圖片，已經convert完了
        self.image, self.rect = load_image()
        #把圖片轉成可以快速貼到螢幕上的形式
        self.image = self.image.convert_alpha()
        self.for_blit = (self.rect.get_width()//2, self.rect.get_height//2)
        pygame.mouse.set_visible(False)
        #初始位置
        self.pos = "自己設定!!!!!!!!!!!!!!!!!!!!!!!!!"
        pygame.mouse.set_pos([x, y])
        screen.blit(self.image, (self.pos[0]-self.for_blit[0], self.pos[1]-self.for_blit[1]))
        #設定玩家血量，然後顯示血條：調整到難易適中，還要再回來設定!!!!!!!!!
        self.blood = 150
        #長150寬20
        self.blood_surface = pygame.Surface((self.blood, 20))
        self.blood_surface.fill((255,0,0))
        self.empty_surface = pygame.Surface((150, 20))
        self.empty_surface.fill((255, 255, 255))
        screen.blits(((self.empty_surface, ("放座標!!!!!")), (self.blood_surface, ("放座標!!!!!"))))
        #然後玩家的初始設定大概差不多就結束了
        self.scream = load_sound("scream.wav")
    def recover(self):
        if self.blood <= 140:
            self.blood += 10
            self.blood_surface = pygame.Surface((self.blood, 20))
            self.blood_surface.fill((255,0,0))
            screen.blits(((empty_surface, ("放座標")), (blood_surface, ("放座標"))))
        else:
            self.blood = 150
            self.blood_surface = pygame.Surface((self.blood, 20))
            self.blood_surface.fill((255,0,0))
            screen.blits(((empty_surface, ("放座標")), (blood_surface, ("放座標"))))


    def injure(self, times):
        #等BTS設定好再來寫
        self.scream.play()
        #血條減少(一次把兩個surface貼上去)
        #這裡要調整難度!!!!!!!!!!!!!!!!!現在可以被摸15次
        self.blood -= 10*times
        if self.blood > 0:
            self.blood_surface = pygame.Surface((self.blood, 20))
            self.blood_surface.fill((255,0,0))
            screen.blits(((empty_surface, ("放座標")), (blood_surface, ("放座標"))))
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
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image()
        self.pos = None
        self.skill = None  #這裡是圖片或其他東西!!!!!!!!冰凍/石化/火焰

    def change_dir(lower, upper):    #再把下面的改一改!!!!!!!!!!!
        direction = random.randint(lower, upper)
        radian = math.radians(direction)
        dx = speed*math.cos(radian)
        dy = speed*math.sin(radian)
        return dx, dy

    def walk(x, y, dx, dy):
        x += dx
        y += dy
        self.rect.move_ip(x, y)
        return x, y

    def skill_n_talk(self):     


    def update(self):
        if 8 <= collide <= 11:    #碰到邊界(只換方向)   還有角落的部分
            if collide == 8:   #上界
                change_dir(180, 360)
                walk(x, y, dx, dy)
    
            if collide == 9:  #下界
                change_dir(0, 180)
                walk(x, y, dx, dy)

            elif collide == 10:   #左界   #支援同界角嗎?
                change_dir(-90, 90)
                walk(x, y, dx, dy)

            else:  #右界
                change_dir(90, 270)
                walk(x, y, dx, dy)
                #之後繼續寫
            
        if 1 <= collide <= 7 or collide == 14 or collide == 15:   #碰到BTS或NPC或隕石 #暫且是14和15!!!!!!!!!
                change_dir(0, 360)
                #之後繼續寫

        if collide == 0:     #碰到玩家


        if collide == -1:    #沒撞到甚麼
            x += dx 
            y += dy
            self.rect.move_ip(x, y)




class NPC(pygame.sprite.Sprite):
    '''
    技能都一樣，差別在於對話框不同
    遇到邊界要後退
    遇到玩家或NPC不能疊上去
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image()
        self.size = (self.image.get_width, self.image.get_height)
        self.x, self.y = None, None #兩個NPC的初始位置不會重疊
        self.speed = 3
        self.up = None
        self.down = None
        self.left = None
        self.right = None

        self.healing = None
        self.healflag = False
        #對話內容
        talk_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 10)
        self.alltalk = None
        
    def Up(self):
        self.y += speed
        self.rect.move_ip(self.x, self.y)
    def Down(self):
        self.y -= speed
        self.rect.move_ip(self.x, self.y)
    def Left(self):
        self.x -= speed
        self.rect.move_ip(self.x, self.y)
    def Right(self):
        self.x += speed
        self.rect.move_ip(self.x, self.y)

    def stepback(self):    
        '''
        碰到障礙物
        這裡要再改!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        '''
        if event1 == self.up:
            self.y -= speed
            self.rect.move_ip(self.x, self.y)
        elif event1 == self.down:
            self.y += speed
            self.rect.move_ip(self.x, self.y)
        elif event1 == self.left:
            self.x += speed
            self.rect.move_ip(self.x, self.y)
        elif event1 == self.right:
            self.x -= speed
            self.rect.move_ip(self.x, self.y)
        else:
            pass
    

    def encounter_player(self):
        '''
        碰到玩家
        '''
        #建立計時器，維持幾秒
        
        #記得回來改!!!!!!!!!!!!
        #維持後要畫回原來的畫面!!!!!!!!!!!!!!

        #先後退
        self.stepback()
        #對話的部分
        #之後再來弄!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        talk_font = pygame.font.Font("game_material/font/HanaMinA.ttf", 12)
        #從一群對話中隨機選出一句，對話放頭上(名字以上)，決定適當的距離!!!!!!!!!!
        self.talk = self.alltalk[random.randint(0, len(self.alltalk)-1)]
        #convert()：建立副本
        self.talk = self.talk.convert()
        #文字框根據對話的長度來決定
        self.talk_bg = pygame.Surface((self.talk.get_width(), self.talk.get_height()))
        screen.blits((self.talk_bg, (self.x, self.y + 10)), (self.talk, (self.x, self.y + 10)))
        pygame.time.wait(5000)
        #把原本的東西全部畫回去!!!!!!!!!!!!!!!!!!!!!!!!!!!


    def update(self):    
                        
    
    
# below is writed by huahua207
# ---------------------------------------------------------------
# load_image and load_sound have been writed by yuarmy.
# now I have to cover the barriers class and border setting.

#創建迷宮物件(這裡我幫你改一下喔!!!!!!!!迷宮還不是一整個視窗，它是視窗裡面的一個Surface物件)
maze_obj = pygame.Surface((790,790))
maze_obj = maze_obj.convert() #convert()建立副本，加快畫布在視窗顯示速度



#background = load_image("mars.jpg") 就load不進來我也不知道為啥嗚嗚嗚嗚
#background.convert()
#screen.blit(background, (20,10))

#創建字體對象
myfont = pygame.font.Font(None, 40)
white = (255,255,255)

class MazeBarrier(pygame.sprite.Sprite):

    def __init__(self, position, texture):
        super().__init__()
        self.texture = texture
        self.image = pygame.surfarray.make_surface(np.transpose(texture ,(1, 0, 2)))
        self.rect = pygame.Rect(position, self.texture.shape[:2])
        # 不太清楚這裡，我想要load image，texture到底是幹嘛用的
    def fire(self): # 用collide去判斷有沒有撞到，有的畫就會觸發這個method
        return
        
# 底圖
class Maze(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image, self.rect = load_image("mars.jpg", "main_pic")
        # 如果load image, type 要怎麼處理？

# 遊戲最最初始值設定，主程式一定是要先跑這個，阿然後可能還要再call NPC and BTS
class MazeGame:

    def __init__(self):
        self.unit = 15

        # The following attributes will be initialized later
        self.maze = None
        self.barriers = []
        self.exit_point = None
        self.Player = Player()
        self.NPC = NPC()
        self.BTS = BTS()

       
        # Build Maze
        with open("maze.txt"), "r") as f:
            # Reserve space for maze
            lines = f.read().strip("\n"),split("\n") # Read the map
            maze = np.zeros(len(lines)*unit, len(lines[0])*unit, 3) # (height, width, depth)

            # Initialize maze row by row
            for row, linr in enumerate(lines):
                for col, symbol in enumerate(line):
                    if symbol == '0': # 障礙物，loadimage進來
                        maze[row*unit:row*unit+unit, col*unit:col*unit+unit, :] = load_image("barrier.png", "main_pic")
                        
                        # Create barrier
                        barrier = MazeBarrier((col*unit, row*unit), maze[row*unit:row*unit+unit, col*unit:col*unit+unit, :].copy())
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
        # Save maze
        self.maze = Maze((0,0),maze.copy())

        # Create groups
        self.barrier_group = pygame.sprite.Group(self.barriers)


#畫東西
pos_x = 300
pos_y = 250
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
        #創建文字
        screen.fill((255,0,0))
        textImage = myfont.render("Welcome to the Mars village.", True, white)
        screen.blit(textImage,(100,100))

        #畫矩形
        color = 255, 190, 0
        width = 0
        pos = pos_x, pos_y, 100, 100
        
        pygame.draw.rect(screen,color,pos,width)
        pygame.display.update()

        #畫圓
        yellow = 255,255,0
        position = 100,250
        radius = 100
        width = 10
        
        pygame.draw.circle(screen, color, position, radius, width)
        pygame.display.update()
# ---------------------------------------------------------------------
# above is writed bt huahua207
