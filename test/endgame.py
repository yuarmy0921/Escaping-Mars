import pygame
import os, sys
from pygame.locals import *
from pygame.compat import geterror

def load_image(name, prev, colorkey = None):
    '''
    把圖片載下來
    '''
    fullname = os.path.join('game_material/'+prev+"/", name)
    try:
        #pygame.image.load(圖片檔案路徑)
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image: ', name)
        raise SystemExit(message)
    #把圖片轉換成最適合呈現的樣子
    image = image.convert()
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
    pygame.init()
    next = False
    screen = pygame.display.set_mode((1440, 800))
    color = (255, 255, 255)
    success_music = load_sound("mikrokosmos.wav")
    success_bg = load_image("success_bg.jpg", "ending_pic")
    success_font = pygame.font.Font("game_material/font/HuaKangXiuFengTiFan/HuaKangXiuFengTiFan.ttf", 30)
    success_s1 = success_font.render("謝謝你救了我們，", True, color)
    success_s2 = success_font.render("以後不管遇到什麼困難，", True, color)
    success_s3 = success_font.render("都請保持著這顆善良而真誠的心堅持下去吧！", True, color)
    text = [success_s1, success_s2, success_s3]
    success_music.play(-1)
    screen.blit(success_bg[0], (0, 0))

    x, y = 140, 200
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
    fail_music = load_sound("so_far_away.wav")
    fail_bg = load_image("fail_bg.png", "ending_pic")
    fail_font = pygame.font.Font("game_material/font/HuaKangXiuFengTiFan/HuaKangXiuFengTiFan.ttf", 30)
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
    fail_music.stop()
    pygame.quit()

main()