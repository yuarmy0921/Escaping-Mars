#建立遊戲環境
import pygame
import random
from Escaping_Mars import *
import math
import os, sys
from pygame.locals import *
from pygame.compat import geterror


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
    instruct2_1 = instruct_font.render("   下左右，碰到NPC即可回血。", True, (255, 255, 255))
    instruct3 = instruct_font.render("3. NPC們都是善良的天使，雖然可能受到精神傷害(", True, (255, 255, 255))
    instruct3_1 = instruct_font.render("   之後就知道為什麼是精神傷害了XD)但必要時還是", True, (255, 255, 255))
    instruct3_2 = instruct_font.render("   向他們求救吧！", True, (255, 255, 255))
    instruct4 = instruct_font.render("4. 在限制時間內保留至少一滴血走到終點", True, (255, 255, 255))
    instruct5 = instruct_font.render("5. 遊戲愉快:D", True, (255, 255, 255))
    
    instruct_set1 = [instruct1, instruct2, instruct2_1, instruct3]
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
#-------------------------------------------------------------------------------------------------------------
    #這是遊戲主要部分!!!!!!!!!!!!!!
    # 重點：所有只出現一段時間的surface都要移除!!!!!!!!!!!!!!
    Game = MazeGame()
    #--這裡是人物設定的部分--------------------------------------------------------------------------------------------------------

    Hua = Game.Player()

    RM = Game.BTS()   #破壞
    RM.image, RM.rect = load_image("koya.png", "main_pic")
    RM.rect[0], RM.rect[1] = 445, 400
    RM.skill = "Dumb: damage"
    RM.sound_flag = True

    Jin = Game.BTS()   #冰凍
    Jin.image, Jin.rect = load_image("rj.png", "main_pic")
    Jin.rect[0], Jin.rect[1] = 460, 420
    Jin.skill = load_image("ice.png", "main_pic")

    Suga = Game.BTS()   #石化
    Suga.image, Suga.rect = load_image("shooky.png", "main_pic")
    Suga.rect[0], Suga.rect[1] = 480, 500
    Suga.skill = load_image("stone.png", "main_pic")

    J_hope = Game.BTS()   #融化
    J_hope.image, J_hope.rect = load_image("mang.png", "main_pic")
    J_hope.rect[0], J-hope.rect[1] = 440, 530
    J-hope.skill = load_image("flame.png", "main_pic")
    J_hope.sound_flag = True

    Jimin = Game.BTS()    #放大
    Jimin.image, Jimin.rect = load_image("chimmy.png", "main_pic")
    Jimin.rect[0], Jimin.rect[1] = 340, 530
    Jimin.skill = False

    V = Game.BTS()    #迷路
    V.image, V.rect = load_image("tata.png", "main_pic")
    V.rect[0], V.rect[1] = 300 ,500
    V.skill = "Dumb: shift"
    V.sound_flag = True

    Jungkook = Game.BTS()   #嗜睡
    Jungkook.image, Jungkook.rect = load_image("cooky.png", "main_pic")
    Jungkook.rect[0], Jung.rect[1] = 310, 420
    Jungkook.sound_flag = True

    BigMac = Game.NPC()
    #初始位置
    #350 480
    BigMac.image, BigMac.rect = load_image("bigmac.png", "main_pic")
    BigMac.rect[0], BigMac.rect[1] = 350, 480
    #設置按鍵
    BigMac.up = K_UP
    BigMac.down = K_DOWN
    BigMac.left = K_LEFT
    BigMac.right = K_RIGHT
    #一個surface物件的LIST
    #BigMac.alltalk = [NPC.talk_font.render(), NPC.talk_font.render(), NPC.talk_font.render()]
    BigMac.healing = K_h

    HongYu = Game.NPC()
    #初始位置
    #420 480
    HongYu.image, HongYu.rect = load_image("hongyu.png", "main_pic")
    HongYu.rect[0], HongYu.rect[1] = 420, 480
    #設置按鍵
    HongYu.up = K_w
    HongYu.down = K_s
    HongYu.left = K_a
    HongYu.right = K_d
    #HongYu.alltalk = [NPC.talk_font.render("你確定你有搞懂自己在幹嘛嗎？", True, (0, 0, 0)), NPC.talk_font.render("唉...", True, (0, 0, 0)), NPC.talk_font.render()]
    HongYu.healing = K_c
    #障礙物和人分開處理
    NPC_group = pygame.sprite.Group(HongYu, BigMac)
    BTS_group = pygame.sprite.Group(RM, Jin, Suga, J_hope, Jimin, V, Jungkook)

    barriers = Game.barrier_group
    
    #--音樂還有背景的部分--------------------------------------------------------------------------------------------------------------
    main_bg = load_image("mars.jpg", "main_pic")
    #把喜歡的歌都放進來吧!!!
    main_bgm_list = ["epiphany", "fake_love", "make_it_right", "save_me", "tomorrow"]
    for i in range(0, len(main_bgm_list)-1):
        main_bgm_list[i] = load_sound(main_bgm[i]+".wav")

    #--------------------------------------------------------------------------------------------------------------------------

    main_bgm = game.main_bgm_list[random.randint(0, len(game.main_bgm_list)-1)]
    main_bgm_channel = main_bgm.play()
    while True:   #這裡的條件還要再另外設定!!!!!!!!!!!!!!!
        if not main_bgm_channel.get_busy():
            main_bgm = game.main_bgm[random.randint(0, len(game.main_bgm_list)-1)]
            main_bgm_channel = main_bgm.play()
        
        #所有事件：上下左右、治療、滑鼠移動(使用道具)
        #隨時更新滑鼠位置
        #處理每一個瞬間場景人物的變化，寶貝們每一秒都在動
        #在一次loop內可能有多個按鍵按下，所以要用for event in pygame.event.get()
        #先移動再判斷有沒有碰到
        #這個部分先處理玩家操作，判斷的部分是後面

        #玩家移動滑鼠的情況
        Hua.walk()

        # NPC的情況
        for event in pygame.event.get():
            if event.type==pygame.QUIT :
                pygame.quit()
            if event.type == KEYDOWN:
                # 這裡是大麥控制
                if event == BigMac.up:
                    BigMac.Up()
                elif event == BigMac.down:
                    BigMac.Down()
                elif event == BigMac.left:
                    BigMac.Left()
                elif event == BigMac.right:
                    BigMac.Right()
                elif event == BigMac.healing:
                    BigMac.healflag = True

                # 這裡是宏宇控制
                elif event == HongYu.up:
                    HongYu.Up()
                elif event == HongYu.down:
                    HongYu.Down()
                elif event == HongYu.left:
                    HongYu.Left()
                elif event == HongYu.right:
                    HongYu.Right()
                elif event == HongYu.healing:
                    HongYu.healflag = True
                else:
                    pass

            # 玩家使用道具的情況，先略過!!!!!!!!!!!!!!!!!!!!!!
            #if event.type == MOUSEBUTTONDOWN:

        #寶貝移動的情況
        for member in BTS_group:
            member.walk()

        #這裡都在判斷碰撞 !!!!!!!!!!!!!!!!!--------------------------------------------------------------------------------------
        #碰撞的情形
        #玩家 障礙物/BTS/NPC
        #BTS BTS/障礙物/NPC
        #NPC NPC/障礙物

        #玩家碰撞到東西
        #先後退
        #障礙物
        if len(pygame.sprite.spritecollide(Hua, barriers)) > 0:
            Hua.stepback()
            Hua.injure(len(pygame.sprite.spritecollide(Hua, barriers)))
            barriers.fire(Hua)

        #BTS
        #放技能
        #玩家受傷(傳入受傷次數)
        if len(pygame.sprite.spritecollide(Hua, BTS_group, False)) > 0:  
            for member in pygame.sprite.spritecollide(Hua, BTS_group, False):
                if member == RM:
                    #破壞
                    Hua.stepback()
                    member.skill_flag = True
                elif member == Jin:
                    #冰凍
                    Hua.stepback()
                    member.skill_flag_pic = True
                elif member == Suga:
                    #石化
                    Hua.stepback()
                    member.skill_flag_pic = True
                elif member == J_hope:
                    #燃燒
                    Hua.stepback()
                    member.skill_flag_pic = True
                elif member == Jimin:
                    #放大
                    Hua.stepback()
                    Jimin.skill_flag = True
                    Hua.image.inflate(1.2, 1.2)
                elif member == V:
                    #瞬移
                    Hua.stepback()
                    member.skill_flag = True
                    Hua.rect[0], Hua.rect[1] = ("起點座標'!!!!!!!")

                elif member == Jungkook:
                    #單純的小孩
                    Hua.stepback()
                    member.skill_flag = True

                else:
                    pass


        #NPC
        if len(pygame.sprite.spritecollide(Hua, NPC_group, False)) > 0:
            for member in pygame.sprite.spritecollide(Hua, NPC_group, False):
                member.stepback()
                if member.healflag:
                    #member.trash_talk()
                    Hua.recover()
                else:
                    pass


        #BTS碰撞到東西
        #互相
        if RM.colliderect(Jin.rect) or RM.colliderect(Suga.rect) or RM.colliderect(J_hope.rect) or RM.colliderect(Jimin.rect) or RM.colliderect(V.rect) or RM.colliderect(Jungkook.rect):
            RM.stepback()
        if Jin.colliderect(Suga.rect) or Jin.colliderect(J_hope.rect) or Jin.colliderect(Jimin.rect) or Jin.colliderect(V.rect) or Jin.colliderect(Jungkook.rect):
            Jin.stepback()
        if Suga.colliderect(J_hope.rect) or Suga.colliderect(Jimin.rect) or Suga.colliderect(V.rect) or Suga.colliderect(Jungkook.rect):
            Suga.stepback()
        if J_hope.colliderect(Jimin.rect) or J_hope.colliderect(V.rect) or J_hope.colliderect(Jungkook.rect):
            J_hope.stepback()
        if Jimin.colliderect(V.rect) or Jimin.colliderect(Jungkook.rect):
            Jimin.stepback()
        if V.colliderect(Jungkook.rect):
            V.stepback()


        #障礙物
        if len(pygame.sprite.groupcollide(BTS_group, barriers, False)) > 0:
            for member in pygame.sprite.groupcollide(BTS_group, barriers, False):
                member.stepback()
                member.change_dir()

        #NPC
        if len(pygame.sprite.groupcollide(NPC_group, BTS_group, False)) > 0:
            for member in pygame.sprite.groupcollide(NPC_group, BTS_group, False):
                member.stepback()

        #NPC碰撞到東西
        #互相
        if BigMac.colliderect(HongYu.rect):
            BigMac.stepback()

        #障礙物
        if len(pygame.sprite.groupcollide(NPC_group, barriers, False)) > 0:
            for member in pygame.sprite.groupcollide(NPC_group, barriers, False):
                member.stepback()
        

        #########儲存上一個位置：判斷後退和移動
        Hua.last_pos = pygame.mouse.get_pos()
        self.last_pos = (self.rect[0], self.rect[1])

        #判斷有沒有碰到成員()
        for member in BTS_group:
            if member.skill_flag_pic:
                #蓋上技能(圖片的部分)
                screen.blit(member.skill[0], (Hua.rect[0], Hua.rect[1]))
                #受傷
                Hua.injure(5, member.sound_flag)
                pygame.time.wait(5000)
                #回復
                screen.blit(Hua.image, Hua.rect)
                member.skill_flag_pic = False
            if member.skill_flag:
                if member == RM:
                    Hua.injure(5, RM.sound_flag)
                else:
                    Hua.scream.play()
                member.skill_flag = False

        #貼上
        Hua.update()
        BTS_group.update()
        NPC_group.update()
        #------------------------------------------------------------------------------------------------------------------------------
        pygame.display.update()
        #判斷死了沒
        if Hua.dead:
            cry = load_sound("cry.wav")
            success_flag = False
            fail_flag = True
            #先關背景音樂
            main_bgm.stop()
            cry.play()
            pygame.time.wait(5000)
            break

        #判斷過關!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if Hua.rect[0] > 1240 and Hua.rect[1] > 770:
            applause = load_sound("applause.wav")
            success_flag = True
            fail_flag = False
            #先關背景音樂
            main_bgm.stop()
            applause.play()
            pygame.time.wait(5000)
            break
    

#-------------------------------------------------------------------------------------------------------------
    #這是過關畫面!!!!!!!
    color = (255, 255, 255)
    while success_flag:
        success_music = load_sound("mikrokosmos.wav")
        success_bg = load_image("success_bg.jpg", "ending_pic")
        success_font = pygame.font.Font("game_material/font/HuaKangXiuFengTiFan/HuaKangXiuFengTiFan.ttf", 20)
        success_s1 = success_font.render("謝謝你救了我們，", True, color)
        success_s2 = success_font.render("以後不管遇到什麼困難，", True, color)
        success_s3 = success_font.render("都請保持著這顆善良而真誠的心堅持下去吧！", True, color)
        text = [success_s1, success_s2, success_s3]
        success_music.play(-1)
        screen.blit(success_bg[0], (0, 0))

        x, y = 140, 300
        for sentence in text:
            screen.blit(sentence, (x, y))
            y += 100
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    next = True
            if next:
                next = False
                break
        success_music.stop()
#--------------------------------------------------------------------------------------------------------------
    #這是失敗畫面QQ
    while fail_flag:
        fail_music = load_sound("so_far_away.wav")
        fail_bg = load_image("fail_bg", "ending_pic")
        fail_font = pygame.font.Font("game_material/font/HuaKangXiuFengTiFan/HuaKangXiuFengTiFan.ttf", 20)
        fail_s1 = fail_font.render("很遺憾你沒有成功，但是也不要太難過，", True, color)
        fail_s2 = fail_font.render("這只是個遊戲，在現實生活中遇到的困難比這個大多了，", True, color)
        fail_s3 = fail_font.render("當遇到挫折的時候請不要輕易放棄，", True, color)
        fail_s4 = fail_font.render("求助於身邊的朋友，即使他們會先恥笑你，", True, color)
        fail_s5 = fail_font.render("但最終還是會拉你一把。", True, color)
        fail_s6 = fail_font.render("如果連你朋友都不幫你的話...", True, color)
        fail_s7 = fail_font.render("   ", True, color)
        fail_s8 = fail_font.render("   ", True, color)
        fail_s9 = fail_font.render("   ", True, color)
        fail_s10 = fail_font.render("   ", True, color)
        fail_s11 = fail_font.render("   ", True, color)
        fail_s12 = fail_font.render("那你就真的沒救了。", True, color)
        text = [fail_s1, fail_s2, fail_s3, fail_s4, fail_s5, fail_s6, fail_s7, fail_s8, fail_s9, fail_s10, fail_s11, fail_s12]
        fail_music.play(-1)
        screen.blit(fail_bg[0], (0, 0))
        x, y = 140, 300
        for sentence in text:
            screen.blit(sentence, (x, y))
            y += 50
        pygame.display.update()
        
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    next = True
            if next:
                break
        fail_music.stop()
#-------------------------------------------------------------------------------------------------
    #結束畫面
    class Ending(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = None 
    ending_music = load_sound("magic_shop.wav")
    ending_bg = load_image("mars.jpg", "main_pic")
    screen.blit(ending_bg[0], (0, 0))
    pygame.display.flip()
    ending_music.play(-1)
    color = (255, 255, 255)
    title_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 20)
    title_font.set_bold(True)
    content_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 15)
    t1 = Ending()
    t1.image = title_font.render("GUI Design", True, color)
    c1 = Ending()
    c1.image = content_font.render("林郁敏", True, color)
    t2 = Ending()
    t2.image = title_font.render("Game Configuration Construction", True, color)
    c2 = Ending()
    c2.image = content_font.render("林郁敏", True, color)
    t3 = Ending()
    t3.image = title_font.render("Character Design", True, color)
    c3 = Ending()
    c3.image = content_font.render("", True, color)
    t4 = Ending()
    t4.image = title_font.render("Character Image", True, color)
    c4 = Ending()
    c4.image = content_font.render("BT21", True, color)
    t5 = Ending()
    t5.image = title_font.render("Maze Design", True, color)
    c5 = Ending()
    c5.image = content_font.render("張悅恩", True, color)
    t6 = Ending()
    t6.image = title_font.render("Background Music", True, color)
    c6 = content_font.render("BTS-Sea     BTS-So far away     BTS-Epiphany     BTS-Magic shop     BTS-Mikrokosmos     BTS-Make it right     BTS-Tomorrow     BTS-Save ME", True, color)
    t7 = Ending()
    t7.image = title_font.render("Special THANKS TO", True, color)
    c7 = Ending()
    c7.image = content_font.render("林宗男 教授     顏宏宇 助教     劉正仁 助教     劉玟慶 助教     郭育昇 助教", True, color)
    ending = Ending()
    ending.image = content_font.render("All rights not reserved", True, color)
    #
    text = [t1, c1, t2, c2, t3, c3, t4, c4, t5, c5, t6, c6, t7, c7, ending]
    x = 200
    y = 100
    for sentence in text:
        screen.blit(sentence.image, (x, y))
        y += 50
    pygame.display.update()
    cal = 0
    while cal <= 1000:
        for sentence in text:
            sentence.move_ip(sentence.rect[0], sentence.rect[1]+10)
        pygame.display.update()
        cal += 100
    ending_music.fadeout(5000)

    pygame.quit()
