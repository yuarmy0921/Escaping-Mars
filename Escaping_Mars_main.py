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
    instruct4 = instruct_font.render("4. 保留至少一滴血走到終點", True, (255, 255, 255))
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
    maze = Game.maze
    barriers = Game.barrier_group
    #--這裡是人物設定的部分--------------------------------------------------------------------------------------------------------

    Hua = Game.player
    #Hua.image, Hua.rect = 
    Hua.screen = screen
    Hua.bighead = pygame.image.load("game_material/main_pic/hua_bighead1.png")
    Hua.pic_rect = pygame.Rect(670, 5, 100, 100)

    RM = Game.bts1  #破壞
    RM.screen = screen
    RM.image, RM.rect = load_image("koya.png", "main_pic")
    RM.rect[0], RM.rect[1] = 720, 280
    RM.skill = "Dumb: damage"
    RM.sound_flag = True

    Jin = Game.bts2   #冰凍
    Jin.screen = screen
    Jin.image, Jin.rect = load_image("rj.png", "main_pic")
    Jin.rect[0], Jin.rect[1] = 790, 300
    Jin.skill = load_image("ice.png", "main_pic")

    Suga = Game.bts3  #石化
    Suga.screen = screen
    Suga.image, Suga.rect = load_image("shooky.png", "main_pic")
    Suga.rect[0], Suga.rect[1] = 790, 380
    Suga.skill = load_image("stone.png", "main_pic")

    J_hope = Game.bts4   #融化
    J_hope.screen = screen
    J_hope.image, J_hope.rect = load_image("mang.png", "main_pic")
    J_hope.rect[0], J_hope.rect[1] = 750, 420
    J_hope.skill = load_image("flame.png", "main_pic")
    J_hope.sound_flag = True

    Jimin = Game.bts5   #放大
    Jimin.screen = screen
    Jimin.image, Jimin.rect = load_image("chimmy.png", "main_pic")
    Jimin.rect[0], Jimin.rect[1] = 690, 420
    Jimin.skill = False

    V = Game.bts6   #迷路
    V.screen = screen
    V.image, V.rect = load_image("tata.png", "main_pic")
    V.rect[0], V.rect[1] = 640, 380
    V.skill = "Dumb: shift"
    V.sound_flag = True

    Jungkook = Game.bts7  #嗜睡
    Jungkook.screen = screen
    Jungkook.image, Jungkook.rect = load_image("cooky.png", "main_pic")
    Jungkook.rect[0], Jungkook.rect[1] = 650, 300
    Jungkook.sound_flag = True

    BigMac = Game.npc1
    BigMac.name = BigMac.name_font.render("大麥", True, (255, 255, 255))
    BigMac.name_rect = pygame.Rect(1375, 110, 50, 20)
    BigMac.screen = screen
    BigMac.bighead = pygame.image.load("game_material/main_pic/bigmac_bighead1.png")
    BigMac.pic_rect = (1335, 5, 100, 100)
    BigMac.talk_frame = load_image("bigmac_talk_frame.png", "main_pic")
    BigMac.talk_frame = BigMac.talk_frame[0]
    BigMac.frame_rect = pygame.Rect(925, 30, 400, 100)
    #初始位置
    #350 480
    BigMac.image, BigMac.rect = load_image("bigmac.png", "main_pic")
    BigMac.rect[0], BigMac.rect[1] = 680, 340
    #設置按鍵
    BigMac.up = K_UP
    BigMac.down = K_DOWN
    BigMac.left = K_LEFT
    BigMac.right = K_RIGHT
    #一個surface物件的LIST
    BigMac.alltalk = [BigMac.talk_font.render("你再一直來的話...我就不理你了QQ", True, (0, 0, 0)), BigMac.talk_font.render("能走到哪就走到哪，誠實面對自己~", True, (0, 0, 0)), BigMac.talk_font.render("可以的~你台大電機的耶!", True, (0, 0, 0))]

    HongYu = Game.npc2
    HongYu.name = HongYu.name_font.render("宏宇", True, (255, 255, 255))
    HongYu.name_rect = pygame.Rect(40, 110, 50, 20)
    HongYu.screen = screen
    HongYu.bighead = pygame.image.load("game_material/main_pic/hongyu_bighead1.png")
    HongYu.pic_rect = pygame.Rect(5, 5, 100, 100)
    HongYu.talk_frame = load_image("hongyu_talk_frame.png", "main_pic")
    HongYu.talk_frame = HongYu.talk_frame[0]
    HongYu.frame_rect = pygame.Rect(115, 30, 400, 100)
    #初始位置
    #420 480
    HongYu.image, HongYu.rect = load_image("hongyu.png", "main_pic")
    HongYu.rect[0], HongYu.rect[1] = 750, 340
    HongYu.up = K_w
    HongYu.down = K_s
    HongYu.left = K_a
    HongYu.right = K_d
    HongYu.alltalk = [HongYu.talk_font.render("你確定你有搞懂自己在幹嘛嗎？", True, (0, 0, 0)), HongYu.talk_font.render("祝同學活得順利。", True, (0, 0, 0)), HongYu.talk_font.render("快死了就要求救，不要拖到最後。", True, (0, 0, 0))]
    #障礙物和人分開處理
    NPC_group = pygame.sprite.Group(HongYu, BigMac)
    BTS_group = pygame.sprite.Group(RM, Jin, Suga, J_hope, Jimin, V, Jungkook)
    
    #--音樂還有背景的部分--------------------------------------------------------------------------------------------------------------
    main_bg = load_image("mars.jpg", "main_pic")
    #把喜歡的歌都放進來吧!!!
    main_bgm_list = ["epiphany", "fake_love", "make_it_right", "save_me", "tomorrow"]
    for i in range(0, len(main_bgm_list)):
        main_bgm_list[i] = load_sound(main_bgm_list[i]+".wav")

    #--------------------------------------------------------------------------------------------------------------------------
    #print(Hua.pos)
    #print(Hua.rect)
    #print(HongYu.up, BigMac.up)
    #print("*"+str(RM.rect[0]))
    main_bgm = main_bgm_list[random.randint(0, len(main_bgm_list)-1)]
    main_bgm_channel = main_bgm.play()
    screen.blit(maze.image, maze.rect)
    screen.blits(((Hua.empty_surface, (570, 110)), (Hua.blood_surface, (570, 110))))
    screen.blits(((Hua.image, Hua.rect), (BigMac.image, BigMac.rect), (HongYu.image, HongYu.rect), (RM.image, RM.rect), (Jin.image, Jin.rect), (Suga.image, Suga.rect), (J_hope.image, J_hope.rect), (Jimin.image, Jimin.rect), (V.image, V.rect), (Jungkook.image, Jungkook.rect)))
    pygame.display.flip()
    
    while True:   #這裡的條件還要再另外設定!!!!!!!!!!!!!!!
        if not main_bgm_channel.get_busy():
            main_bgm = main_bgm_list[random.randint(0, len(main_bgm_list)-1)]
            main_bgm_channel = main_bgm.play()

        # NPC的情況
        for event in pygame.event.get():
            """print(event)"""
            #print(Hua.pos)
            #print(Hua.last_pos)
            if event.type == pygame.QUIT :
                pygame.quit()
            #玩家移動滑鼠的情況
            elif event.type == MOUSEMOTION:
                #滑鼠移動到哪就馬上移動到哪
                Hua.pos = event.pos
                Hua.walk()
                
            elif event.type == KEYDOWN:
                # 這裡是大麥控制
                if event.key == K_UP:       
                    BigMac.Up()
                    """print("Previous:", BigMac.prev)"""
                elif event.key == BigMac.down:
                    BigMac.Down()
                elif event.key == BigMac.left:
                    BigMac.Left()
                elif event.key == BigMac.right:
                    BigMac.Right()
            
                # 這裡是宏宇控制
                elif event.key == HongYu.up:
                    HongYu.Up()
                elif event.key == HongYu.down:
                    HongYu.Down()
                elif event.key == HongYu.left:
                    HongYu.Left()
                elif event.key == HongYu.right:
                    HongYu.Right()
                else:
                    pass
            else:
                pass  
            """print("Bigmac position:", BigMac.rect)"""
            # 玩家使用道具的情況，先略過!!!!!!!!!!!!!!!!!!!!!!
            #if event.type == MOUSEBUTTONDOWN:

        #寶貝移動的情況
        for member in BTS_group:
            member.walk()

        #把圖片技能圖片換回來:
        if Hua.image != Hua.save_image:
            Hua.image = Hua.save_image
            screen.blit(Hua.image, Hua.rect)
            pygame.display.update(Hua.rect)
        #這裡都在判斷碰撞 !!!!!!!!!!!!!!!!!--------------------------------------------------------------------------------------
        #碰撞的情形
        #玩家 障礙物/BTS/NPC
        #BTS BTS/障礙物/NPC
        #NPC NPC/障礙物

        #玩家碰撞到東西
        hua_barrier = pygame.sprite.spritecollide(Hua, barriers, False)
        hua_bts = pygame.sprite.spritecollide(Hua, BTS_group, False)
        hua_npc = pygame.sprite.spritecollide(Hua, NPC_group, False)
        #先後退
        #障礙物
        
        if len(hua_barrier) > 0:
            #print("Collide with barriers"+str(len(hua_barrier)))
            #for item in hua_barrier:
                #print(item)
            Hua.stepback()
            Hua.injure(len(hua_barrier), True)
            screen.blit(main_bg[0], main_bg[1])
            screen.blit(maze.image, maze.rect)
            screen.blits(((Hua.empty_surface, (570, 110)), (Hua.blood_surface, (570, 110))))
            pygame.display.flip()
            BTS_group.update()
            NPC_group.update()
            hua_barrier = []

        #BTS
        #放技能
        #玩家受傷(傳入受傷次數)
        if len(hua_bts) > 0:  
            for member in hua_bts:
                if member == RM:
                    #破壞
                    member.stepback()
                    member.skill_flag = True
                elif member == Jin:
                    #冰凍
                    member.stepback()
                    member.skill_flag_pic = True
                elif member == Suga:
                    #石化
                    member.stepback()
                    member.skill_flag_pic = True
                elif member == J_hope:
                    #燃燒
                    member.stepback()
                    member.skill_flag_pic = True
                elif member == Jimin:
                    #放大
                    member.stepback()
                    Jimin.skill_flag = True
                    #Hua.image.inflate(1.2, 1.2)
                elif member == V:
                    #瞬移
                    member.stepback()
                    member.skill_flag = True
                    Hua.rect[0], Hua.rect[1] = Hua.start[0], Hua.start[1]
                    screen.blit(main_bg[0], main_bg[1])
                    screen.blit(maze.image, maze.rect)
                    screen.blits(((Hua.empty_surface, (570, 110)), (Hua.blood_surface, (570, 110))))
                    pygame.mouse.set_pos([Hua.rect[0], Hua.rect[1]])
                    screen.blit(Hua.image, Hua.rect)
                    pygame.display.flip()
                    BTS_group.update()
                    NPC_group.update()

                elif member == Jungkook:
                    #單純的小孩
                    member.stepback()
                    member.skill_flag = True

                else:
                    pass
            hua_bts = []

        #NPC
        if len(hua_npc) > 0:
            for member in hua_npc:
                member.talk_flag = True
                temp_pos = pygame.mouse.get_pos()
                member.stepback()
                member.stepback()
                member.stepback()
                member.trash_talk()
                Hua.recover()
                pygame.mouse.set_pos(temp_pos)
                Hua.rect[0], Hua.rect[1] = temp_pos[0], temp_pos[1]
                pygame.display.update(Hua.rect)
            hua_npc = []


        #BTS碰撞到東西
        bts_barrier = pygame.sprite.groupcollide(BTS_group, barriers, False, False)
        bts_npc = pygame.sprite.groupcollide(NPC_group, BTS_group, False, False)
        #互相
        
        if RM.rect.colliderect(Jin.rect) or RM.rect.colliderect(Suga.rect) or RM.rect.colliderect(J_hope.rect) or RM.rect.colliderect(Jimin.rect) or RM.rect.colliderect(V.rect) or RM.rect.colliderect(Jungkook.rect):
            RM.stepback()
            RM.change_dir()
        if Jin.rect.colliderect(Suga.rect) or Jin.rect.colliderect(J_hope.rect) or Jin.rect.colliderect(Jimin.rect) or Jin.rect.colliderect(V.rect) or Jin.rect.colliderect(Jungkook.rect):
            Jin.stepback()
            Jin.change_dir()
        if Suga.rect.colliderect(J_hope.rect) or Suga.rect.colliderect(Jimin.rect) or Suga.rect.colliderect(V.rect) or Suga.rect.colliderect(Jungkook.rect):
            Suga.stepback()
            Suga.change_dir()
        if J_hope.rect.colliderect(Jimin.rect) or J_hope.rect.colliderect(V.rect) or J_hope.rect.colliderect(Jungkook.rect):
            J_hope.stepback()
            J_hope.change_dir()
        if Jimin.rect.colliderect(V.rect) or Jimin.rect.colliderect(Jungkook.rect):
            Jimin.stepback()
            Jimin.change_dir()
        if V.rect.colliderect(Jungkook.rect):
            V.stepback()
            V.change_dir()


        #障礙物
        if len(bts_barrier) > 0:
            for member in bts_barrier:
                member.stepback()
                member.change_dir()
            bts_barrier = []

        #NPC
        if len(bts_npc) > 0:
            for member in bts_npc:
                member.stepback()
            bts_npc = []

        #NPC碰撞到東西
        npc_barrier = pygame.sprite.groupcollide(NPC_group, barriers, False, False)
        #互相
        if BigMac.rect.colliderect(HongYu.rect):
            BigMac.stepback()

        #障礙物
        if len(npc_barrier) > 0:
            for member in npc_barrier:
                member.stepback()
            npc_barrier = []

        #########儲存上一個位置：判斷後退和移動
        Hua.last_pos = pygame.mouse.get_pos()
        Hua.rect[0], Hua.rect[1] = Hua.last_pos[0], Hua.last_pos[1]
        screen.blit(main_bg[0], main_bg[1])
        screen.blit(maze.image, maze.rect)
        screen.blits(((Hua.empty_surface, (570, 110)), (Hua.blood_surface, (570, 110))))
        pygame.display.flip()
        BTS_group.update()
        NPC_group.update()
        
        #判斷有沒有碰到成員()
        for member in BTS_group:
            if member.skill_flag_pic:
                #蓋上技能(圖片的部分)
                #有bug!!!!!!!!!!!!
                Hua.image = member.skill[0]
                #受傷
                Hua.injure(5, member.sound_flag)
                pygame.mouse.set_pos([Hua.rect[0], Hua.rect[1]])
                #回復
                #screen.blit(Hua.image, Hua.rect)
                #pygame.display.update(Hua.rect)
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
        #print("Blood:"+str(Hua.blood))
        #print(pygame.mouse.get_pos())
        #print(Hua.last_pos)
        #print(Hua.pos)
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
        Hua.last_pos = pygame.mouse.get_pos()
        """print(Hua.last_pos)"""
        Hua.rect[0], Hua.rect[1] = Hua.last_pos
        """print("finish:", Hua.rect)"""
        if Hua.rect[0] > Hua.finish[0] and Hua.rect[1] > Hua.finish[1]:
            applause = load_sound("applause.wav")
            success_flag = True
            fail_flag = False
            #先關背景音樂
            main_bgm.stop()
            applause.play()
            pygame.time.wait(5000)
            break
    next = False
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                next = True
                break
        if next:
            next = False
            break
#-------------------------------------------------------------------------------------------------------------
    #這是過關畫面!!!!!!!
    pygame.mouse.set_visible(True)
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
        success_flag = False
        success_music.stop()
#--------------------------------------------------------------------------------------------------------------
    #這是失敗畫面QQ
    while fail_flag:
        black = pygame.surface.Surface((1440, 800))
        black.fill((0, 0, 0))
        fail_music = load_sound("so_far_away.wav")
        fail_bg = load_image("fail_bg.jpg", "ending_pic")
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
        screen.blit(black, (0, 0))
        screen.blit(fail_bg[0], (0, 0))
        x, y = 140, 200
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
        fail_flag = False
        fail_music.stop()
#-------------------------------------------------------------------------------------------------
    #結束畫面
    class Title(pygame.sprite.Sprite):
        def __init__(self, title, y):
            pygame.sprite.Sprite.__init__(self)
            title_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 20)
            title_font.set_bold(True)
            self.image = title_font.render(title, True, (255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect[0], self.rect[1] = 720-self.rect[2]//2, y
    class Content(pygame.sprite.Sprite):
        def __init__(self, content, y):
            pygame.sprite.Sprite.__init__(self)
            content_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 15)
            self.image = content_font.render(content, True, (255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect[0], self.rect[1] = 720-self.rect[2]//2, y
    ending_music = load_sound("magic_shop.wav")
    ending_bg = load_image("mars.jpg", "main_pic")
    screen.blit(ending_bg[0], (0, 0))
    pygame.display.flip()
    ending_music.play(-1)
    
    t1 = Title("Team Member", 400)
    c1 = Content("張悅恩   林郁敏", 450)
    
    t2 = Title("GUI Design", 550)
    c2 = Content("林郁敏", 600)

    t3 = Title("Game Configuration Construction", 700)
    c3 = Content("林郁敏", 750)

    t4 = Title("Character Code", 850)
    c4 = Content("林郁敏", 900)

    t5 = Title("Maze Code", 1000)
    c5 = Content("張悅恩", 1050)

    t6 = Title("Maze Design", 1150)
    c6 = Content("張悅恩", 1200)

    t7 = Title("Material Resources", 1300)
    c7_1 = Content("Character images(BTS): BT21 Copyright © LINE Corporation All rights reserved", 1350)
    c7_2 = Content("Character image(Hua Chen Yu): https://zhidao.baidu.com/question/525270507842709245.html", 1400)
    c7_3 = Content("Dialogue frame: Vector Designed By Windy from https://zh.pikbest.com/graphic-elements/hand-drawn-info-box-dialog-design-elements_1151025.html", 1450)
    c7_4 = Content("Background picture(success): BTS official facebook", 1500)
    c7_5 = Content("Background picture(fail): https://www.cobaltrecruitment.com/news-blog/item/life-on-mars", 1550)

    t8 = Title("Background Music", 1650)
    c8 = Content("BTS-Sea    BTS-So far away    BTS-Epiphany    BTS-Magic shop    BTS-Mikrokosmos    BTS-Make it right    BTS-Tomorrow    BTS-Save ME", 1700)
    
    t9 = Title("Special THANKS TO", 1800)
    c9 = Content("林宗男 教授     顏宏宇 助教     劉正仁 助教     劉玟慶 助教     郭育昇 助教", 1850)
    ending = Content("All rights reserved", 1950)
    #
    text = [t1, c1, t2, c2, t3, c3, t4, c4, t5, c5, t6, c6, t7, c7_1, c7_2, c7_3, c7_4, c7_5, t8, c8, t9, c9, ending]

    cal = 0
    while cal <= 2000:
        screen.blit(ending_bg[0], (0, 0))
        for sentence in text:
            #print(sentence.rect[0], sentence.rect[1])
            if sentence.rect[1] > 0:
                sentence.rect.move_ip(0, -1)
                screen.blit(sentence.image, (sentence.rect[0], sentence.rect[1]))  
                print(sentence.rect)
            
        pygame.display.update()
        pygame.time.wait(10)
        cal += 1
    ending_music.fadeout(5000)
    pygame.time.wait(5000)
    pygame.display.quit()
main()