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
        def __init__(self, title):
            pygame.sprite.Sprite.__init__(self)
            title_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 20)
            title_font.set_bold(True)
            self.image = title_font.render(title, True, (255, 255, 255))
            self.rect = self.image.get_rect()
    class Content(pygame.sprite.Sprite):
        def __init__(self, content):
            pygame.sprite.Sprite.__init__(self)
            content_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 15)
            self.image = content_font.render(content, True, (255, 255, 255))
            self.rect = self.image.get_rect()
    ending_music = load_sound("magic_shop.wav")
    ending_bg = load_image("mars.jpg", "main_pic")
    screen.blit(ending_bg[0], (0, 0))
    pygame.display.flip()
    ending_music.play(-1)
    
    t1 = Title("Team Member")
    c1 = Content("張悅恩   林郁敏")
    
    t2 = Title("GUI Design")
    c2 = Content("林郁敏")

    t3 = Title("Game Configuration Construction")
    c3 = Content("林郁敏")

    t4 = Title("Character Code")
    c4 = Content("林郁敏")

    t5 = Title("Maze Code")
    c5 = Content("張悅恩")

    t6 = Title("Maze Design")
    c6 = Content("張悅恩")

    t7 = Title("Material Resources")
    c7_1 = Content("Character images(BTS): BT21 Copyright © LINE Corporation All rights reserved")
    c7_2 = Content("Character image(Hua Chen Yu): https://zhidao.baidu.com/question/525270507842709245.html")
    c7_3 = Content("Dialogue frame: Vector Designed By Windy from https://zh.pikbest.com/graphic-elements/hand-drawn-info-box-dialog-design-elements_1151025.html")
    c7_4 = Content("Background picture(success): BTS official facebook")
    c7_5 = Content("Background picture(fail)")

    t8 = Title("Background Music")
    c8 = Content("BTS-Sea    BTS-So far away    BTS-Epiphany    BTS-Magic shop    BTS-Mikrokosmos    BTS-Make it right    BTS-Tomorrow    BTS-Save ME")
    
    t9 = Title("Special THANKS TO")
    c9 = Content("林宗男 教授     顏宏宇 助教     劉正仁 助教     劉玟慶 助教     郭育昇 助教")
    ending = Content("All rights reserved")
    #
    text = [t1, c1, t2, c2, t3, c3, t4, c4, t5, c5, t6, c6, t7, c7_1, c7_2, c7_3, c7_4, c7_5, t8, c8, t9, c9, ending]

    
    y = 100
    judge = False
    for sentence in text:
        sentence.rect[0], sentence.rect[1] = 720-sentence.rect[2]//2, y
        #print(sentence.rect[0], sentence.rect[1])
        if not judge:
            y += 50
            if 1050 <= y <= 1200:
                judge = False
            else:
                judge = True
        else:
            y += 100
            judge = False
    cal = 0
    while cal <= 2000:
        screen.blit(ending_bg[0], (0, 0))
        for sentence in text:
            #print(sentence.rect[0], sentence.rect[1])
            if sentence.rect[1] > 0:
                sentence.rect.move_ip(0, -1)
                screen.blit(sentence.image, (sentence.rect[0], sentence.rect[1]))  
            
        pygame.display.update()
        pygame.time.wait(10)
        cal += 1
    ending_music.fadeout(5000)
    pygame.time.wait(5000)
    pygame.display.quit()
main()