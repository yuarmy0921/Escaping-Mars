import pygame
import random
#from Escaping_Mars import *
import math
import os, sys
from pygame.locals import *
from pygame.compat import geterror

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


#玩家
#遊戲程序：先有一段故事背景，然後再正式進入遊戲，在進入之前滑鼠還不能換成圖片
#blit：把元素貼到windows視窗上
#rect用來偵測事件，要同時把image和rect貼到windows上

'''
class Player(pygame.sprite.Sprite):
    
    #隨著滑鼠移動
    #碰到迷宮邊界則損血，碰到隕石也損血
    #碰到NPC回血

    
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
        
        #玩家狀態
        
        pos = pygame.mouse.get_pos()
        self.rect.mid = pos


    
class BTS(pygame.sprite.Sprite):
    
    #不用管分別的技能是甚麼，反正只要碰到就損血，另外寫碰到玩家時的行為
    #特效另外放
    #南俊：破壞/碩珍：冰凍/玧其：石化/號錫：融化/
    #智旻：放大/泰亨：迷路/柾國：嗜睡

    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image()
        init_pos = None
        self.skill = None  #這裡是圖片!!!!!!!!冰凍/石化/火焰

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


        if collide == -1:    #沒撞到甚麼
            x += dx 
            y += dy
            self.rect.move_ip(x, y)



class NPC(pygame.sprite.Sprite):
    
    #技能都一樣，差別在於對話框不同
    #遇到邊界要後退
    #遇到玩家或NPC不能疊上去
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image()
        self.size = (self.image.get_width, self.image.get_height)
        self.x, self.y = None, None #兩個NPC的初始位置不會重疊
        speed = 3
        self.up = None
        self.down = None
        self.left = None
        self.right = None

        self.healing = None

        self.content = None
        
    def talk_n_heal(self):
        #建立計時器，維持幾秒
        #convert()：建立副本
        #記得回來改!!!!!!!!!!!!
        #維持後要畫回原來的畫面!!!!!!!!!!!!!!
        talk_font = pygame.font.Font("game_material/font/HanaMinA.ttf", 12)
        #從一群對話中隨機選出一句，對話放頭上(名字以上)，決定適當的距離!!!!!!!!!!
        conversation = talk_font.render(random.randint(0, len(self.content)-1), )
        #這邊先看情況!!!!!!!!!!
        temp_image, temp_rect = None, None
        screen.blit(conversation, (self.x, self.y + 10))
        pygame.display.update()
        pygame.time.wait(5000)
        #把原本的東西全部畫回去!!!!!!

    def update(self):    #一直按著可以一直前進，但要考慮碰到玩家的情況，記得clamp在邊界和迷宮裡面
        #只要偵測每一瞬間有沒有移動
        #This will get all the messages and remove them from the queue.
        for event1 in pygame.event.get():     #這個東西只能偵測外接應體的情況#The input queue is heavily dependent on the pygame.displaypygame module to control the display window and screen module. 
            if event1.type == KEYDOWN:   #移動的情況，同時按兩個鍵!!!!!!!!!!!!!!!!!
                for event2 in pygame.event.get():
                    if event2.type != KEYUP:     #還沒放開
                        if self.rect.collidelist(interact_obj) == -1:   #沒碰到任何東西
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
                        elif self.rect.collidelist(interact_obj) == 0: #碰到玩家
                            if pygame.event.poll() == self.healing:
                                if event1 == self.up:
                                    self.y -= speed
                                    self.rect.move_ip(self.x, self.y)
                                    #這裡要呼叫玩家回血同時放出對話!!!!!!!!
                                    talk_n_heal()
                                    #回血!!!!!!!!!


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

                        else:   #有碰到玩家以外的東西東西要後退
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

#創建窗口(這裡我幫你改一下喔!!!!!!!!迷宮還不是一整個視窗，它是視窗裡面的很多Surface物件)
maze_obj = pygame.Surface.set_mode((790,790))
maze_obj = maze_obj.convert() #convert()建立副本，加快畫布在視窗顯示速度



#background = load_image("mars.jpg") 就load不進來我也不知道為啥嗚嗚嗚嗚
#background.convert()
#screen.blit(background, (20,10))

#創建字體對象
myfont = pygame.font.Font(None, 40)
white = (255,255,255)

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

def load_image(name, prev, colorkey = None):
    
    把圖片載下來
    
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

def load_music(name):
    #如果沒有成功載入音樂就不撥放
    class NoneMusic:
        def play(self): pass
    #pygame.mixer：撥放音樂的module
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('game_material/voice/', name)
    print(fullname)
    try:
        #create a new sound object
        music = pygame.mixer.music.load(fullname)
    except pygame.error as message:
        print('Cannot load a music: ', name)
        raise SystemExit(message)
    return music


    
    
    























#迷宮主體
#路障
#隕石


def main():
    #--------------------------------------------------------------------------------------------------------------------
    #問題：去背圖檔colorkey的設定!!!!!!!!!!!!!!!!!!!!!!!!
    pygame.init()
    pygame.mixer.init(channels = 6)
    #pygame.font.init()
    #pygame.display.init()
    screen_size = (1440, 900)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Escaping Mars")
#---------------------------------------------------------------------------------------------------------------
    #這是初始畫面
    #while前面是設定的部分
    init_bg = load_image("mars.png", "init_pic")
    #再決定要用甚麼音樂，這是一個音樂object
    init_bgm = load_music("sea.mp3")
    caption_font = pygame.font.Font("game_material/font/NIGHTMARE/Nightmare.ttf", 100)
    dumb = pygame.font.Font("game_material/font/Conserta/Conserta.ttf", 60)
    #字體顏色之後再來調!!!!!!!!
    caption = caption_font.render("Escaping Mars", True, (255, 255, 255))
    tbc = dumb.render("Click to continue", True, (255, 255, 255))
    init_bgm.play(-1)   #infinite play music
    screen.blits(((init_bg[0], (0, 0)), (caption, (140, 90)), (tbc, (240, 600))))
    pygame.display.flip()
    next = None
    while True:
        #畫出螢幕
        #等待使用者按下按鍵
        #Returns a sequence of booleans representing the state of all the mouse buttons.
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                next = True
        if next:
            break
#----------------------------------------------------------------------------------------------------------------
    #這是story畫面
    #要放文字框和NPC圖!!!!!!!!!!!!
    #最後記得拿掉
    #記得回來改字體大小!!!!!!!!!!
    next = False
    story_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 30)

    caption = caption_font.render("Story", True, (255, 255, 255))
    story_line1 = story_font.render("    你是火星村的村長，某一天不知道發生甚麼事，火星村", True, (255, 255, 255))
    story_line2 = story_font.render("村民都瘋了！他們開始漫無目的地亂走並且開始攻擊人！你", True, (255, 255, 255))
    story_line3 = story_font.render("深愛著你的村民們，不希望攻擊回去並且開始想盡辦法逃出", True, (255, 255, 255))
    story_line4 = story_font.render("火星村，如此一來才能拿到解藥並且拯救他們。", True, (255, 255, 255))
    #對話框停留直到玩家按下按鍵
    #畫出背景圖，左上角座標
    screen.blits(((init_bg[0], (0, 0)), (caption, (140, 90))))
    #記得回來設座標!!!!!!!!!!!!!!!!!!!
    x = 140
    y = 300
    for sentence in story:
        screen.blit(sentence, (x, y))
        y += 100

    pygame.display.flip()
    while True:
        for event in pygame.event.get():  #等待(還沒按下按鍵則在這個loop裡面停留)
            if event.type == MOUSEBUTTONDOWN:
                next = True
                break
        if next:
            next = False
            break
#----------------------------------------------------------------------------------------------------------------
    #這是instruction畫面!!!!!!!!!!!
    caption = caption_font.render("Instruction", True, (255, 255, 255))
    instruct_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 30)
    instruct1 = instruct_font.render("1. 使用滑鼠控制人物，注意不要碰到邊界，會受傷QQ", True, (255, 255, 255))
    instruct2 = instruct_font.render("2. NPC是可以控制的，移動方式分別是WASD和上下左右，", True, (255, 255, 255))
    instruct2_1 = instruct_font.render("   治療方式分別是C和H，在碰到玩家時按下按鍵可施予治療", True, (255, 255, 255))
    instruct3 = instruct_font.render("3. NPC們都是善良的天使，雖然可能受到精神傷害XD但必要時", True, (255, 255, 255))
    instruct3_1 = instruct_font.render("   還是向他們求救吧！", True, (255, 255, 255))
    instruct4 = instruct_font.render("4. 在限制時間內保留至少一滴血走到終點", True, (255, 255, 255))
    instruct5 = instruct_font.render("5. 遊戲愉快:D", True, (255, 255, 255))
    instruct = [instruct1, instruct2, instruct2_1, instruct3, instruct3_1, instruct4, instruct5]
    #一定要照順序貼到螢幕上!!!!!
    screen.blits(((init_bg[0], (0, 0)), (caption, (140, 90))))
    x = 140
    y = 300
    for item in instruct:
        screen.blit(item, (x, y))
        y += 100

    pygame.display.flip()
    while True:
        for event in pygame.event.get():  #等待(還沒按下按鍵則在這個loop裡面停留)
            if event.type == MOUSEBUTTONDOWN:
                next = True
                break
        if next:
            #關掉第一首音樂
            init_bgm.stop()
            next = False
            break

    pygame.quit()

main()


#這是BTS的
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