#建立遊戲環境
import pygame
import random
from Escaping_Mars import *
import math
import os, sys
from pygame.locals import *
from pygame.compat import geterror


def main():
    Hua = Player()

    RM = BTS()   #破壞
    RM.skill = 
    Jin = BTS()   #冰凍
    Jin.skill = load_image("ice.png", "main_pic")
    Suga = BTS()   #石化
    Suga.skill = load_image("stone.png", "main_pic")
    J_hope = BTS()   #融化
    J-hope.skill = load_image("flame.png", "main_pic")
    Jimin = BTS()    #放大
    Jimin.skill = Hua.mouse_image.inflate(1.5, 1.5)
    V = BTS()    #迷路
    V.skill = "大哥哥我迷路了QQ你可以帶我回家嗎?"
    Jungkook = BTS()   #嗜睡
    Jungkook.skill = "Zzz..."
    '''
    BTS_members = pygame.sprite.Group(RM, Jin, Suga, J_hope, Jimin, V, Jungkook)
    '''

    BigMac = NPC()
    '''
    BigMac.x = 
    BigMac.y = 
    '''
    BigMac.up = K_UP
    BigMac.down = K_DOWN
    BigMac.left = K_LEFT
    BigMac.right = K_RIGHT
    BigMac.talk.content = ["你不要一直受傷...不然...我就不理你了QQ"]
    BigMac.healing = K_h

    HongYu = NPC()
    '''
    HongYu.x = 
    HongYu.y = 
    '''
    HongYu.up = K_w
    HongYu.down = K_s
    HongYu.left = K_a
    HongYu.right = K_d
    HongYu.talk.content = ["你確定你有搞懂自己在幹嘛嗎？", "唉..."]
    HongYu.healing = K_c
    #注意這裡還有些變數沒定義!!!!!!!!
    interact_obj = [Hua.rect, RM.rect, Jin.rect, Suga.rect, J_hope.rect, Jimin.rect, V.rect, Jungkook.rect, bound_u.rect, bound_d.rect, bound_l.rect, bound_r.rect, wall, meteorite.rect, BigMac.rect, HongYu.rect]


    #--------------------------------------------------------------------------------------------------------------------
    #問題：對話沒有出現  背景音樂要轉成wav  去背圖檔colorkey的設定!!!!!!!!!!!!!!!!!!!!!!!!
    pygame.init()
    pygame.font.init()
    pygame.display.init()
    pygame.mixer.init()
    screen_size = (1440, 900)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Escaping Mars")
#---------------------------------------------------------------------------------------------------------------
    #這是初始畫面
    #while前面是設定的部分
    init_bg = load_image("mars.png", "init_pic")
    #再決定要用甚麼音樂，這是一個音樂object
    init_bgm = load_sound("sea.wav")
    caption_font = pygame.font.Font("game_material/font/NIGHTMARE/Nightmare.ttf", 100)
    dumb = pygame.font.Font("game_material/font/Conserta/Conserta.ttf", 40)
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
    init_HongYu = load_image("HongYu.png", "init_pic")
    init_BigMac = load_image("BigMac.png", "init_pic")
    story_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 30)
    saying_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 20)

    caption = caption_font.render("Story", True, (255, 255, 255))
    story_line1 = story_font.render("    你是火星村的村長，某一天不知道發生", True, (255, 255, 255))
    story_line2 = story_font.render("甚麼事，火星村村民都瘋了！他們開始漫無目", True, (255, 255, 255))
    story_line3 = story_font.render("的地亂走並且開始攻擊人！你深愛著你的村民", True, (255, 255, 255))
    story_line4 = story_font.render("們，不希望攻擊回去並且開始想盡辦法逃出火", True, (255, 255, 255))
    story_line5 = story_font.render("星村，如此一來才能拿到解藥並且拯救他們。", True, (255, 255, 255))
    story = [story_line1, story_line2, story_line3, story_line4, story_line5]
    saying = saying_font.render("雖然你看起來不怎麼樣，但我還是會盡量幫助你啦", True, (255, 255, 255))
    #對話框停留直到玩家按下按鍵
    #畫出背景圖，左上角座標
    screen.blits(((init_bg[0], (0, 0)), (caption, (140, 90)), (init_HongYu[0], (100, 255))))
    #記得回來設座標!!!!!!!!!!!!!!!!!!!
    x = 760
    y = 220
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
            break

    next = False
    screen.blit(saying, (300, 300))
    #更新是指螢幕上的"某塊區域"
    pygame.display.update(saying.get_rect())
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
    instruct_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 25)
    instruct1 = instruct_font.render("1. 使用滑鼠控制人物，注意不要碰到邊界，會受傷QQ", True, (255, 255, 255))
    instruct2 = instruct_font.render("2. NPC是可以控制的，移動方式分別是WASD和上下左右", True, (255, 255, 255))
    instruct2_1 = instruct_font.render("   ，治療方式分別是C和H，在碰到玩家時按下按鍵可施予治療", True, (255, 255, 255))
    instruct3 = instruct_font.render("3. NPC們都是善良的天使，雖然可能受到精神傷害XD但必要時", True, (255, 255, 255))
    instruct3_1 = instruct_font.render("   還是向他們求救吧！", True, (255, 255, 255))
    instruct4 = instruct_font.render("4. 在限制時間內保留至少一滴血走到終點", True, (255, 255, 255))
    instruct5 = instruct_font.render("5. 遊戲愉快:D", True, (255, 255, 255))
    instruct = [instruct1, instruct2, instruct2_1, instruct3, instruct3_1, instruct4, instruct5]

    saying = saying_font.render("能力到哪就走到哪，誠實面對自己~", True, (255, 255, 255))

    init_BigMac = load_image("BigMac.png", "init_pic")

    #一定要照順序貼到螢幕上!!!!!
    screen.blits(((init_bg[0], (0, 0)), (caption, (140, 90)), (init_BigMac[0], (100, 255))))
    x = 700
    y = 220
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
            break
    next = False
    screen.blit(saying, (300, 300))
    #更新是指螢幕上的"某塊區域"
    pygame.display.update(saying.get_rect())
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
#-------------------------------------------------------------------------------------------------------------
    #這是遊戲主要部分!!!!!!!!!!!!!!
    #先貼背景圖
    #然後匯入迷宮
    main_bg = load_image("mars.jpg", "main_pic")
    #把喜歡的歌都放進來吧!!!
    main_bgm = ["epiphany", "fake_love", "magic_shop", "make_it_right", "mikrokosmos", "save_me", "so_far_away", "tomorrow"]
    for i in len(main_bgm):
        main_bgm[i] = load_sound(main_bgm[i])
    #每一首放完要隨機選下一首
    #如何偵測音樂撥放完?(隨時偵測)：如果
    main_bgm[random.randint(0, len(main_bgm)-1)].play()
    screen
#-------------------------------------------------------------------------------------------------------------
    #這是過關畫面!!!!!!!
    def success():

#--------------------------------------------------------------------------------------------------------------
    #這是失敗畫面QQ
    def fail():
'''    
