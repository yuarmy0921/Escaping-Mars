import pygame
import random
from Escaping_Mars import *
import math
import os, sys
from pygame.locals import *
from pygame.compat import geterror
import cv2
import numpy as np

def main():
    pygame.init()
    pygame.font.init()
    pygame.display.init()
    pygame.mixer.init(channels = 6)
    screen_size = (1440, 800)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Escaping Mars")
    quit_flag = False
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
        
        #所有事件：上下左右、治療、滑鼠移動(使用道具)
        #隨時更新滑鼠位置
        #處理每一個瞬間場景人物的變化，寶貝們每一秒都在動
        #在一次loop內可能有多個按鍵按下，所以要用for event in pygame.event.get()
        #先移動再判斷有沒有碰到
        #這個部分先處理玩家操作，判斷的部分是後面
        

        # NPC的情況
        for event in pygame.event.get():
            print(event)
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
                    print("Previous:", BigMac.prev)
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
            print("Bigmac position:", BigMac.rect)
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
            #for barrier in barriers:
                #barrier.fire()
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
                    #Hua.image.inflate(1.2, 1.2)
                elif member == V:
                    #瞬移
                    Hua.stepback()
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
                    Hua.stepback()
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
            if event.type == KEYDOWN:
                next = True
                break
        if next:
            next = False
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
        pygame.quit()
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
                if event.type == KEYDOWN:
                    next = True
            if next:
                break
        fail_music.stop()
        pygame.quit()
#-------------------------------------------------------------------------------------------------
main()