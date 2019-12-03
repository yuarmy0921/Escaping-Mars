import pygame
import os, sys
from pygame.locals import *
from pygame.compat import geterror
#載入遊戲：還要再回來檢查
#pygame.image.load()預設得到的type是surface
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
        pygame.draw.rect(blood_surface, )
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
    寶貝們的技能
    不用管分別的技能是甚麼，反正只要碰到就損血，另外寫碰到玩家時的行為
    特效另外放
    要不要能穿牆
    #寶貝們
    #南俊：破壞/碩珍：冰凍/玧其：石化/號錫：融化/
    智旻：/泰亨：迷路/柾國：嗜睡

    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image()

    

    def skill(self):

    def update(self):


RM = BTS()
Jin = BTS()
Suga = BTS()
J_hope = BTS()
Jimin = BTS()
V = BTS()
Jungkook = BTS()

class NPC(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = 

    def rescue(self):

    def update()

BigMac = NPC()
HongYu = NPC()

    
    
    




#兩個NPC
#大麥：可愛能量/





#迷宮主體
#路障
#隕石
