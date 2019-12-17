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
    fullname = os.path.join('game_material'+prev+"/", name)
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
    try:
        #create a new sound object
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print('Cannot load a sound: ', wav)
        raise SystemExit(message)
    return sound

#玩家
#遊戲程序：先有一段故事背景，然後再正式進入遊戲，在進入之前滑鼠還不能換成圖片
#blit：把元素貼到windows視窗上
#rect用來偵測事件，要同時把image和rect貼到windows上


class Player(pygame.sprite.Sprite):
    '''
    隨著滑鼠移動
    碰到迷宮邊界則損血，碰到隕石也損血
    碰到NPC回血

    '''
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        #被取代成滑鼠的圖片，已經convert完了
        self.mouse_image, self.mouse_rect = load_image()
        #這裡我也不知道在幹嘛!!!!!!!!!!!
        self.mouse_image.convert_alpha()
        pygame.mouse.set_visible(False)
        self.position = position
        #這裡的screen變數要再協調好，這還是一個未被定義的變數!!!!!!!!!!!!!!!!!
        screen.blit(self.mouse_image, self.mouse_rect)
        #設定玩家血量，然後顯示血條：調整到難易適中，還要再回來設定!!!!!!!!!
        self.life = 500
        blood_surface = pygame.Surface()
        #紅色滿血：還要再回來設定!!!!!!!!!!
        blood_surface.fill((255,0,0))
        #然後玩家的初始設定大概差不多就結束了

    def recover(self):
        #設定好與NPC相遇的條件
        #所有的事件都要自己定義好
        #隨時偵測滑鼠的位置
        #等NPC設定好再來寫

    def injure(self):
        #等BTS設定好再來寫

    def update(self):
        '''
        玩家狀態
        '''
        pos = pygame.mouse.get_pos()
        self.rect.mid = pos


    
class BTS(pygame.sprite.Sprite):
    '''
    不用管分別的技能是甚麼，反正只要碰到就損血，另外寫碰到玩家時的行為
    特效另外放
    #南俊：破壞/碩珍：冰凍/玧其：石化/號錫：融化/
    智旻：放大/泰亨：迷路/柾國：嗜睡

    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image()
        init_pos = None

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

    def skill(self):     #這裡只有說話的部分

    def update(self):
        collide = self.rect.collidelist(interact_obj)
        if collide != -1:   #有撞到東西
            if 8 <= collide <= 11:    #碰到邊界(只換方向)   還有角落的部分
                if collide == 8:   #上界
                    change_dir(180, 360)
                    walk(x, y, dx, dy)
    
                elif collide == 9:  #下界
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

            if #撞到牆!!!!!!:

        if collide == -1:    #沒撞到甚麼
            x += dx 
            y += dy
            self.rect.move_ip(x, y)



class NPC(pygame.sprite.Sprite):
    '''
    技能都一樣，差別在於對話框不同
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image()
        self.x, self.y = None, None #兩個NPC的初始位置不會重疊
        speed = 3
        #設定對話(optional)
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        
    def talk(self):
        #建立計時器，維持幾秒
        #convert()：建立副本
        #記得回來改!!!!!!!!!!!!
        talk_font = pygame.font.Font("game_material/font/HanaMinA.ttf", 12)

    def update(self):    #一直按著可以一直前進，但要考慮碰到玩家的情況，記得clamp在邊界和迷宮裡面
        #只要偵測每一瞬間有沒有移動
        #This will get all the messages and remove them from the queue.
        for event1 in pygame.event.get():     #這個東西只能偵測外接應體的情況#The input queue is heavily dependent on the pygame.displaypygame module to control the display window and screen module. 
            if event1.type == KEYDOWN:   #移動的情況
                for event2 in pygame.event.get():
                    if event2.type != KEYUP and (self.rect.collidelist(interact_obj) < 1 or self.rect.collidelist(interact_obj) > 7):     #還沒放開而且沒碰到玩家
                        if event1 == self.up:
                            self.y += speed
                            self.rect.move_ip(self.x, self.y)
                        elif event1 == self.down:
                            self.y -= speed
                            self.rect.move_ip(self.x, self.y)
                        elif event1 == self.left:
                            self.x -= speed
                            self.rect.move_ip(self.x, self.y)
                        elif event1 == self.right:
                            self.x += speed
                            self.rect.move_ip(self.x, self.y)
                        else:
                            pass
            elif event1.type == 
                    




        #位置的資料型態是tuple嗎???
        #讓人物的rect一直移動：持續畫出新的螢幕
        #方向等迷宮長相確定好了再來設定

            if collide == 0:     #碰到玩家
                #先停下不要動
                #然後跳出對話框，填入文字，這個狀態維持幾秒鐘，記得再回來設定對話框大小!!!!!!
                talk(self)
                #等玩家回血!!!!!!!!之後再回來寫!!!!!!!!!!!
                #換個方向離開
                

            if #撞到牆!!!!!!!!!!!!:
                continue

        

    
    
    
# below is writed by huahua207
# ---------------------------------------------------------------
# load_image and load_sound have been writed by yuarmy.
# now I have to cover the barriers class and border setting.

#blit：把元素貼到windows視窗上
#rect用來偵測事件，要同時把image和rect貼到windows上


#初始化pygame
pygame.init()

#創建窗口(這裡我幫你改一下喔!!!!!!!!迷宮還不是一整個視窗，它是視窗裡面的很多Surface物件)
maze_obj = pygame.Surface.set_mode((790,790))
maze_obj = maze_obj.convert() #convert()建立副本，加快畫布在視窗顯示速度



#background = load_image("mars.jpg") 就load不進來我也不知道為啥嗚嗚嗚嗚
#background.convert()
#screen.blit(background, (20,10))

#創建字體對象
myfont = pygame.font.Font(None, 40)
white = 255,255,255

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
        self.image, self.rect = load_image(mars.jpg, colorkey)
        # 如果load image, type 要怎麼處理？

# 遊戲最最初始值設定，主程式一定是要先跑這個，阿然後可能還要再call NPC and BTS
class MazeGame:

    def __init__(self):
        self.unit = 15

        # The following attributes will be initialized later
        self.maze = None
        self.player = None
        self.barriers = []
        self.exit_point = None

        # Build Maze
        with open("maze.txt"), "r") as f:
            # Reserve space for maze
            lines = f.read().strip("\n"),split("\n") # Read the map
            maze = np.zeros(len(lines)*unit, len(lines[0])*unit, 3) # (height, width, depth)

            # Initialize maze row by row
            for row, linr in enumerate(lines):
                for col, symbol in enumerate(line):
                    if symbol == '0': # 障礙物，loadimage進來
                        maze[row*unit:row*unit+unit, col*unit:col*unit+unit, :] = load_image("barrier.png")
                        
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
        self.player_group = pygame.sprite.Group(self.player)
        self.barrier_group = pygame.sprite.Group(self.barriers)


#畫東西
pygame.display.set_caption("畫東西")
pos_x = 300
pos_y = 250
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
        #創建文字
        screen.fill((255,0,0))
        textImage = myfont.render("Welcome to the Mars village.", True,white)
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



    
    
    























#迷宮主體
#路障
#隕石
