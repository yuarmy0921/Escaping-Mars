import pygame
from Escaping_Mars import




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
BigMac.talk.content = 
HongYu = NPC()
#這裡改成load_image的形式!!!!!!!!!!!
HongYu.talk.content = ["你確定你有搞懂自己在幹嘛嗎？", "唉..."]
#注意這裡還有些變數沒定義!!!!!!!!
interact_obj = [Hua.rect, RM.rect, Jin.rect, Suga.rect, J_hope.rect, Jimin.rect, V.rect, Jungkook.rect, bound_u.rect, bound_d.rect, bound_l.rect, bound_r.rect, wall, meteorite.rect, BigMac.rect, HongYu.rect]
def main():
    pygame.init()
    screen_size = (1280, 1024)
    #創建遊戲視窗
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Escaping Mars")

    def start_surface():
        #開始流程：click to continue/Story line/Instruction/start
        #反正就是先把所有需要的圖片抓進來
        #還有音樂
        init_bg = load_image("mars.png", "init_pic")
        init_npc1 = 
        init_npc2 = 
        #再決定要用甚麼音樂
        init_bgm = load_sound("")
        #change the pixel format of an image
        init_bg = init_bg.convert()
        init_npc1 = init_npc1.convert()
        init_npc2 = init_npc2.convert()
        





        #一起貼到視窗上
        screen.blit()
    def game_surface():