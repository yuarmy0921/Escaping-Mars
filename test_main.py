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
    #pygame.font.init()
    #pygame.display.init()
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
    #--這裡是人物設定的部分--------------------------------------------------------------------------------------------------------

    Hua = Game.player
    Hua.image, Hua.rect = load_image("huahua.png","main_pic")
    Hua.screen = screen

    RM = Game.bts1  #破壞
    RM.screen = screen
    RM.image, RM.rect = load_image("koya.png", "main_pic")
    RM.rect[0], RM.rect[1] = 460, 380
    RM.skill = "Dumb: damage"
    RM.sound_flag = True

    Jin = Game.bts2   #冰凍
    Jin.screen = screen
    Jin.image, Jin.rect = load_image("rj.png", "main_pic")
    Jin.rect[0], Jin.rect[1] = 530, 400
    Jin.skill = load_image("ice.png", "main_pic")

    Suga = Game.bts3  #石化
    Suga.screen = screen
    Suga.image, Suga.rect = load_image("shooky.png", "main_pic")
    Suga.rect[0], Suga.rect[1] = 530, 480
    Suga.skill = load_image("stone.png", "main_pic")

    J_hope = Game.bts4   #融化
    J_hope.screen = screen
    J_hope.image, J_hope.rect = load_image("mang.png", "main_pic")
    J_hope.rect[0], J_hope.rect[1] = 490, 520
    J_hope.skill = load_image("flame.png", "main_pic")
    J_hope.sound_flag = True

    Jimin = Game.bts5   #放大
    Jimin.screen = screen
    Jimin.image, Jimin.rect = load_image("chimmy.png", "main_pic")
    Jimin.rect[0], Jimin.rect[1] = 430, 520
    Jimin.skill = False

    V = Game.bts6   #迷路
    V.screen = screen
    V.image, V.rect = load_image("tata.png", "main_pic")
    V.rect[0], V.rect[1] = 380, 480
    V.skill = "Dumb: shift"
    V.sound_flag = True

    Jungkook = Game.bts7  #嗜睡
    Jungkook.screen = screen
    Jungkook.image, Jungkook.rect = load_image("cooky.png", "main_pic")
    Jungkook.rect[0], Jungkook.rect[1] = 390, 400
    Jungkook.sound_flag = True

    BigMac = Game.npc1
    BigMac.screen = screen
    #初始位置
    #350 480
    BigMac.image, BigMac.rect = load_image("bigmac.png", "main_pic")
    BigMac.rect[0], BigMac.rect[1] = 420, 440
    #設置按鍵
    BigMac.up = K_UP
    BigMac.down = K_DOWN
    BigMac.left = K_LEFT
    BigMac.right = K_RIGHT
    #一個surface物件的LIST
    #BigMac.alltalk = [NPC.talk_font.render(), NPC.talk_font.render(), NPC.talk_font.render()]
    BigMac.healing = K_h

    HongYu = Game.npc2
    HongYu.screen = screen
    #初始位置
    #420 480
    HongYu.image, HongYu.rect = load_image("hongyu.png", "main_pic")
    HongYu.rect[0], HongYu.rect[1] = 490, 440
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
    for i in range(0, len(main_bgm_list)):
        main_bgm_list[i] = load_sound(main_bgm_list[i]+".wav")

    #--------------------------------------------------------------------------------------------------------------------------
    
    main_bgm = main_bgm_list[random.randint(0, len(main_bgm_list)-1)]
    main_bgm_channel = main_bgm.play()
    screen.blit(maze.image, maze.rect)
    screen.blits(((Hua.life, (330, 35)), (Hua.empty_surface, (400, 50)), (Hua.blood_surface, (400, 50))))
    screen.blits(((Hua.image, Hua.rect), (BigMac.image, BigMac.rect), (HongYu.image, HongYu.rect), (RM.image, RM.rect), (Jin.image, Jin.rect), (Suga.image, Suga.rect), (J_hope.image, J_hope.rect), (Jimin.image, Jimin.rect), (V.image, V.rect), (Jungkook.image, Jungkook.rect)))
    pygame.display.flip()
    next = False
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                next = True
                break
        if next:
            next = False
            break
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
        if len(pygame.sprite.spritecollide(Hua, barriers, False)) > 0:
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
        Hua.last_pos = (Hua.rect[0], Hua.rect[1])

        screen.blit(maze.image, maze.rect)
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
                if event.type == MOUSEBUTTONDOWN:
                    next = True
            if next:
                break
        fail_music.stop()
        pygame.quit()
#-------------------------------------------------------------------------------------------------
main()