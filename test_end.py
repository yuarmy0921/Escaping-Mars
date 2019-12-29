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
    screen = pygame.display.set_mode((1440, 800))
    ending_music = load_sound("magic_shop.wav")
    ending_bg = load_image("mars.jpg", "ending_pic")
    screen.blit(ending_bg[0], (0, 0))
    pygame.display.flip()
    ending_music.play(-1)
    #-----------------------------------------------------------------------------
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
    
    t1 = Title("Team Member", 550)
    c1 = Content("張悅恩   林郁敏", 600)
    
    t2 = Title("GUI Design", 700)
    c2 = Content("林郁敏", 750)

    t3 = Title("Game Configuration Construction", 850)
    c3 = Content("林郁敏", 900)

    t4 = Title("Character Code", 1000)
    c4 = Content("林郁敏", 1050)

    t5 = Title("Maze Code", 1150)
    c5 = Content("張悅恩", 1200)

    t6 = Title("Maze Design", 1300)
    c6 = Content("張悅恩", 1350)

    t7 = Title("Material Resources", 1450)
    c7_1 = Content("Character images(BTS): BT21 Copyright © LINE Corporation All rights reserved", 1500)
    c7_2 = Content("Character image(Hua Chen Yu): https://zhidao.baidu.com/question/525270507842709245.html", 1550)
    c7_3 = Content("Dialogue frame: Vector Designed By Windy from https://zh.pikbest.com/graphic-elements/hand-drawn-info-box-dialog-design-elements_1151025.html", 1600)
    c7_4 = Content("Background picture(success): BTS official facebook", 1650)
    c7_5 = Content("Background picture(fail): https://www.cobaltrecruitment.com/news-blog/item/life-on-mars", 1700)

    t8 = Title("Background Music", 1800)
    c8 = Content("BTS-Sea    BTS-So far away    BTS-Epiphany    BTS-Magic shop    BTS-Mikrokosmos    BTS-Make it right    BTS-Tomorrow    BTS-Save ME", 1850)
    
    t9 = Title("Special THANKS TO", 400)
    c9 = Content("林宗男 教授     顏宏宇 助教     劉正仁 助教     劉玟慶 助教     郭育昇 助教", 450)
    ending = Content("All rights reserved", 1650)
    #
    text = [t1, c1, t2, c2, t3, c3, t4, c4, t5, c5, t6, c6, t7, c7_1, c7_2, c7_3, c7_4, c7_5, t8, c8, t9, c9, ending]

    cal = 0
    while cal <= 1000:
        screen.blit(ending_bg[0], (0, 0))
        for sentence in text:
            #print(sentence.rect[0], sentence.rect[1])
            if sentence.rect[1] > 0:
                sentence.rect.move_ip(0, -1)
                screen.blit(sentence.image, (sentence.rect[0], sentence.rect[1]))  
                print(sentence.rect)
            else:
                text.remove(sentence)
        print(text)
        pygame.display.update()
        pygame.time.wait(10)
        cal += 1
    ending_music.fadeout(5000)
    pygame.time.wait(5000)
    pygame.display.quit()
main()