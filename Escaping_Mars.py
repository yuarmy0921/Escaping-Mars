import pygame
import random 
import math
import os, sys
from pygame.locals import *
from pygame.compat import geterror
#載入遊戲：還要再回來檢查
#pygame.image.load()預設得到的type是surface
#pygame.sprite.Group.update：call the update method
def load_image(name, colorkey = None):
    '''
    把圖片載下來
    '''
    fullname = os.path.join('data', name)
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
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
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
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #被取代成滑鼠的圖片，已經convert完了
        self.mouse_image, self.mouse_rect = load_image()
        #這裡我也不知道在幹嘛!!!!!!!!!!!
        self.mouse_image.convert_alpha()
        pygame.mouse.set_visible(False)
        #設定玩家初始位置：再回來改!!!!!!!!!!!!!!!!!
        init_pos = 
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

Hua = Player()
    
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


RM = BTS()   #破壞
Jin = BTS()   #冰凍
Suga = BTS()   #石化
J_hope = BTS()   #融化
Jimin = BTS()    #放大
V = BTS()    #迷路
Jungkook = BTS()   #嗜睡
BTS_members = pygame.sprite.Group(RM, Jin, Suga, J_hope, Jimin, V, Jungkook)

class NPC(pygame.sprite.Sprite):
    '''
    技能都一樣，差別在於對話框不同
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #記得分別兩個人的對話圖片!!!!!!!!!!!
        self.image, self.rect = load_image()
        x, y = None #兩個NPC的初始位置不會重疊
        #設定對話(optional)
        speed = 3
    
        #圖片要鏡像反射嗎?在碰到牆的瞬間換圖片：pygame.transform.flip
        
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

    def talk(self):
        #建立計時器，維持幾秒
        #convert()：建立副本
        talk_surface = pygame.Surface()
        talk_surface = talk_surface.convert()  #確認一下這是幹嘛用的!!!!!!
        talk_surface.fill((255,255,255))
        #這裡有還沒定義的視窗變數!!!!!!!!!!!!
        screen.blit(talk_surface, #這裡要擺位置座標)
        talk_surface.display.update()

    def update(self):    #一次update是一個畫格，每一瞬間都在update
        collide = self.rect.collidelist(interact_obj)
        if collide != -1:   #有撞到東西
            if 8 <= collide <= 11:    #碰到邊界(只換方向)   還有角落的部分
                if collide == 8:   #上界
                    change_dir(180, 360)
                    walk(x, y, dx, dy)  #先移動一點點，確保不會判斷錯誤
    
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



        #位置的資料型態是tuple嗎???
        #讓人物的rect一直移動：持續畫出新的螢幕
        #方向等迷宮長相確定好了再來設定

            if collide == 0:     #碰到玩家
                #先停下不要動
                #然後跳出對話框，填入文字，這個狀態維持幾秒鐘，記得再回來設定對話框大小!!!!!!
                #自己建立對話框文字圖片(不支援中文)
                talk(self)
                #等玩家回血!!!!!!!!之後再回來寫!!!!!!!!!!!
                #換個方向離開
                change_dir(0, 360)
                walk(x, y, dx, dy)
                #之後繼續寫!!!!!!!!!!

            if #撞到牆!!!!!!!!!!!!:
                continue

        if collide == -1:     #沒撞到甚麼
           walk(x, y, dx, dy)

BigMac = NPC()
BigMac.talk.content = 
HongYu = NPC()
#這裡改成load_image的形式!!!!!!!!!!!
HongYu.talk.content = ["你確定你有搞懂自己在幹嘛嗎？", "唉..."]
#注意這裡還有些變數沒定義!!!!!!!!
interact_obj = [Hua.rect, RM.rect, Jin.rect, Suga.rect, J_hope.rect, Jimin.rect, V.rect, Jungkook.rect, bound_u.rect, bound_d.rect, bound_l.rect, bound_r.rect, wall, meteorite.rect, BigMac.rect, HongYu.rect]


# below is writed by huahua207
# ---------------------------------------------------------------
# load_image and load_sound have been writed by yuarmy.
# now I have to cover the barriers class and border setting.

#blit：把元素貼到windows視窗上
#rect用來偵測事件，要同時把image和rect貼到windows上

class barriers(pygame.sprite.Sprite):
    """
    BTS不可以穿越barriers
    player碰到會損血
    player碰到必須有火花或是火焰，這個再匯入image即可
    """
    def __init__(self,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        #self.image, self.rect = load_image(barrier.png, colorkey)
        self.rect.center = (pos_x, pos_y) #位置
    def being_touch(self):
        return
    def fire(self):
        fires = []
        for i in range(3):
             fire.image, fire.rect = load_image(檔案,colorkey)
             fires.append(fire)
        return

#初始化pygame
pygame.init()

#創建窗口
screen = pygame.display.set_mode((790,790))
screen = screen.convert() #convert()建立副本，加快畫布在視窗顯示速度

#載入圖片
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

#background = load_image("mars.jpg") 就load不進來我也不知道為啥嗚嗚嗚嗚
#background.convert()
#screen.blit(background, (20,10))

#創建字體對象
myfont = pygame.font.Font(None, 40)
white = 255,255,255

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
