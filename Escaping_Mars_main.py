#建立遊戲環境
import pygame
from Escaping_Mars.py import *




Hua = Player()

RM = BTS()   #破壞
Jin = BTS()   #冰凍
Suga = BTS()   #石化
J_hope = BTS()   #融化
Jimin = BTS()    #放大
V = BTS()    #迷路
Jungkook = BTS()   #嗜睡
BTS_members = pygame.sprite.Group(RM, Jin, Suga, J_hope, Jimin, V, Jungkook)

BigMac = NPC()
BigMac.up = K_UP
BigMac.down = K_DOWN
BigMac.left = K_LEFT
BigMac.right = K_RIGHT
BigMac.talk.content = 

HongYu = NPC()
HongYu.x = 
HongYu.y = 
HongYu.up = K_w
HongYu.down = K_s
HongYu.left = K_a
HongYu.right = K_d
HongYu.talk.content = ["你確定你有搞懂自己在幹嘛嗎？", "唉..."]
#注意這裡還有些變數沒定義!!!!!!!!
interact_obj = [Hua.rect, RM.rect, Jin.rect, Suga.rect, J_hope.rect, Jimin.rect, V.rect, Jungkook.rect, bound_u.rect, bound_d.rect, bound_l.rect, bound_r.rect, wall, meteorite.rect, BigMac.rect, HongYu.rect]
def main():
    pygame.init()
    pygame.font.init()
    pygame.display.init()
    screen_size = (1280, 1024)
    #創建遊戲視窗
    #這也是一個Surface
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Escaping Mars")
#---------------------------------------------------------------------------------------------------------------
    #這是初始畫面
    #pygame.display.update(rect)
    #blit之後還要再display(double buffer)
    #while前面是設定的部分
    #開始流程：click to continue/Story line/Instruction/start
    #反正就是先把所有需要的圖片抓進來，注意rect
    #還有音樂
    #init_bg是一個tuple(image, rect)
    init_bg = load_image("mars.png", "init_pic")
    #再決定要用甚麼音樂，這是一個音樂object
    init_bgm = load_sound("")
    #先使用預設字體，之後再來改成漂亮的!!!!!!
    #調整大小
    #撥放音樂
    caption_font = pygame.font.Font("arial", 20)
    dumb = pygame.font.Font("arial", 10)
    #字體顏色之後再來調!!!!!!!!
    caption = caption_font.render("Escaping Mars", True, (255, 255, 255))
    init_bgm.play(-1)   #infinite play music
    while True:
        #畫出螢幕
        #等待使用者按下按鍵
        #Returns a sequence of booleans representing the state of all the mouse buttons.
        screen.blit(init_bg[0], (0, 0))
        for event in pygame.event,get():
            if event.type == MOUSEBUTTONDOWN:
                next = True
                break
        if next:
            break
#----------------------------------------------------------------------------------------------------------------
    #這是story畫面
    #要放文字框和NPC圖!!!!!!!!!!!!
    #最後記得拿掉
    #記得回來改字體大小!!!!!!!!!!
    next = False
    init_HongYu = load_image()
    init_BigMac = load_image()
    story_font = pygame.font.Font("game_material/font/HanaMinA.ttf", 12)
    saying_font = pygame.font.Font("game_material/font/HanaMinA.ttf", 16)

    caption = caption_font.render("Instruction", True, (255, 255, 255))
    story_line1 = story_font.render("    你是火星村的村長，某一天不知道發生", True, (255, 255, 255))
    story_line2 = story_font.render("甚麼事，火星村村民都瘋了！他們開始漫無目", True, (255, 255, 255))
    story_line3 = story_font.render("的地亂走並且開始攻擊人！你深愛著你的村民", True, (255, 255, 255))
    story_line4 = story_font.render("們，不希望攻擊回去並且開始想盡辦法逃出火", True, (255, 255, 255))
    story_line5 = story_font.render("星村，如此一來才能拿到解藥並且拯救他們。", True, (255, 255, 255))
    story = list(story_line1, story_line2, story_line3, story_line4, story_line5)
    saying = saying_font.render("雖然你看起來不怎麼樣，但我還是會盡量幫助你啦", True, (, ,))
    #對話框停留直到玩家按下按鍵
    #畫出背景圖，左上角座標
    screen.blits((init_bg[0], (0, 0)), (caption, ()), (init_HongYu[0], ()))
    #記得回來設座標!!!!!!!!!!!!!!!!!!!
    x = 
    y = 
    for sentence in story:
        screen.blit(sentence, (x, y))
        y += 

    screen.display.flip()
    while True:
        for event in pygame.event.get():  #等待(還沒按下按鍵則在這個loop裡面停留)
            if event.type == MOUSEBUTTONDOWN:
                next = True
                break
        if next:
            break

    next = False
    screen.blit(saying, ())
    #更新是指螢幕上的"某塊區域"
    screen.display.update(saying.get_rect())
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
    #記得去下載英文字體!!!!!!!!!!!!!
    #最後記得再換一張圖!!!!!!!!
    #先把必要元素都指定好
    caption = caption_font.render("Instruction", True, (255, 255, 255))
    instruct_font = pygame.font.Font("game_material/font/HanaMinA.ttf", 12)
    instruct1 = instruct_font.render("", True, (255, 255, 255))
    instruct2 = instruct_font.render("", True, (255, 255, 255))
    instruct3 = instruct_font.render("", True, (255, 255, 255))
    instruct4 = instruct_font.render("", True, (255, 255, 255))
    instruct = list(instruct1, instruct2, instruct3, instruct4)

    saying = saying_font.render("", True, (255, 255, 255))

    init_BigMac = load_image("", )

    #一定要照順序貼到螢幕上!!!!!
    screen.blits((init_bg[0], (0, 0)), (caption, #位置), (init_BigMac[0], ()))
    x = 
    y = 
    for item in instruct:
        screen.blit(item, (x, y))
        y += 

    screen.display.flip()
    while True:
        for event in pygame.event.get():  #等待(還沒按下按鍵則在這個loop裡面停留)
            if event.type == MOUSEBUTTONDOWN:
                next = True
                break
        if next:
            break
    next = False
    screen.blit(saying, ())
    #更新是指螢幕上的"某塊區域"
    screen.display.update(saying.get_rect())
    while True:
        for event in pygame.event.get():  #等待(還沒按下按鍵則在這個loop裡面停留)
            if event.type == MOUSEBUTTONDOWN:
                next = True
                break
        if next:
            next = False
            break
#-------------------------------------------------------------------------------------------------------------
    #這是遊戲主要部分!!!!!!!!!!!!!!

