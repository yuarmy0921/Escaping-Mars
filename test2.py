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

def load_image(name, prev, colorkey = None):
    
    #把圖片載下來
    
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


def main():
    #--------------------------------------------------------------------------------------------------------------------
    #問題：去背圖檔colorkey的設定!!!!!!!!!!!!!!!!!!!!!!!!
    pygame.init()
    #pygame.font.init()
    #pygame.display.init()
    pygame.mixer.init(channels = 6)
    screen_size = (1440, 800)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Escaping Mars")
    quit_flag = False
#---------------------------------------------------------------------------------------------------------------
    #這是初始畫面
    #while前面是設定的部分
    init_bg = load_image("mars.png", "init_pic")
    #再決定要用甚麼音樂，這是一個音樂object
    init_bgm = load_sound("sea.wav")
    caption_font = pygame.font.Font("game_material/font/NIGHTMARE/Nightmare.ttf", 150)
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
    subcaption_font = pygame.font.Font("game_material/font/NIGHTMARE/Nightmare.ttf", 100)
    story_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 30)

    subcaption = subcaption_font.render("Story", True, (255, 255, 255))
    story_line1 = story_font.render("    你是火星村的村長，某一天不知道發生甚麼事，火星村", True, (255, 255, 255))
    story_line2 = story_font.render("村民都瘋了！他們開始漫無目的地亂走並且開始攻擊人！你", True, (255, 255, 255))
    story_line3 = story_font.render("深愛著你的村民們，不希望攻擊回去並且開始想盡辦法逃出", True, (255, 255, 255))
    story_line4 = story_font.render("火星村，如此一來才能拿到解藥並且拯救他們。", True, (255, 255, 255))
    story = [story_line1, story_line2, story_line3, story_line4]
    #對話框停留直到玩家按下按鍵
    #畫出背景圖，左上角座標
    screen.blits(((init_bg[0], (0, 0)), (subcaption, (140, 90))))
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
    subcaption = subcaption_font.render("Instruction", True, (255, 255, 255))
    instruct_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 30)
    instruct1 = instruct_font.render("1. 使用滑鼠控制人物，注意不要碰到邊界，會受傷QQ", True, (255, 255, 255))
    instruct2 = instruct_font.render("2. NPC是可以控制的，移動方式分別是WASD和上", True, (255, 255, 255))
    instruct2_1 = instruct_font.render("   下左右，治療方式分別是C和H，在碰到玩家時按下", True, (255, 255, 255))
    instruct2_2 =instruct_font.render("   按鍵可施予治療", True, (255, 255, 255))
    instruct3 = instruct_font.render("3. NPC們都是善良的天使，雖然可能受到精神傷害(", True, (255, 255, 255))
    instruct3_1 = instruct_font.render("   之後就知道為什麼是精神傷害了XD)但必要時還是", True, (255, 255, 255))
    instruct3_2 = instruct_font.render("   向他們求救吧！", True, (255, 255, 255))
    instruct4 = instruct_font.render("4. 在限制時間內保留至少一滴血走到終點", True, (255, 255, 255))
    instruct5 = instruct_font.render("5. 遊戲愉快:D", True, (255, 255, 255))
    
    instruct_set1 = [instruct1, instruct2, instruct2_1, instruct2_2, instruct3]
    instruct_set2 = [instruct3_1, instruct3_2, instruct4, instruct5]
    screen.blits(((init_bg[0], (0, 0)), (subcaption, (140, 90))))
    x = 140
    y = 300
    for item in instruct_set1:
        screen.blit(item, (x, y))
        y += 100
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                next = True
                break
        if next:
            next = False
            break
    x = 140
    y = 300
    #這裡要移除上一段instruct!!!!!!!!!!
    screen.blits(((init_bg[0], (0, 0)), (subcaption, (140, 90))))
    
    for item in instruct_set2:
        screen.blit(item, (x, y))
        y += 100
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
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