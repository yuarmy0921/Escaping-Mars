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
    print('enter main')
    pygame.init()
    print("flag")
    screen = pygame.display.set_mode((1440, 800))
    class Ending(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = None 
            self.rect = None
    ending_music = load_sound("magic_shop.wav")
    ending_bg = load_image("mars.jpg", "ending_pic")
    screen.blit(ending_bg[0], (0, 0))
    pygame.display.flip()
    print("flag")
    ending_music.play(-1)
    #-----------------------------------------------------------------------------
    print("flag")
    color = (255, 255, 255)
    title_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 20)
    title_font.set_bold(True)
    content_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 15)
    print("flag")
    t1 = Ending()
    t1.image = title_font.render("GUI Design", True, color)
    t1.rect = t1.image.get_rect()

    c1 = Ending()
    c1.image = content_font.render("林郁敏", True, color)
    c1.rect = c1.image.get_rect()

    t2 = Ending()
    t2.image = title_font.render("Game Configuration Construction", True, color)
    t2.rect = t2.image.get_rect()

    c2 = Ending()
    c2.image = content_font.render("林郁敏", True, color)
    c2.rect = c2.image.get_rect()

    t3 = Ending()
    t3.image = title_font.render("Character Design", True, color)
    t3.rect = t3.image.get_rect()

    c3 = Ending()
    c3.image = content_font.render("", True, color)
    c3.rect = c3.image.get_rect()

    t4 = Ending()
    t4.image = title_font.render("Character Image", True, color)
    t4.rect = t4.image.get_rect()

    c4 = Ending()
    c4.image = content_font.render("BT21", True, color)
    c4.rect = c4.image.get_rect()

    t5 = Ending()
    t5.image = title_font.render("Maze Design", True, color)
    t5.rect = t5.image.get_rect()

    c5 = Ending()
    c5.image = content_font.render("張悅恩", True, color)
    c5.rect = c5.image.get_rect()

    t6 = Ending()
    t6.image = title_font.render("Background Music", True, color)
    t6.rect = t6.image.get_rect()

    c6 = Ending()
    c6.image = content_font.render("BTS-Sea     BTS-So far away     BTS-Epiphany     BTS-Magic shop     BTS-Mikrokosmos     BTS-Make it right     BTS-Tomorrow     BTS-Save ME", True, color)
    c6.rect = c6.image.get_rect()

    t7 = Ending()
    t7.image = title_font.render("Special THANKS TO", True, color)
    t7.rect = t7.image.get_rect()

    c7 = Ending()
    c7.image = content_font.render("", True, color)
    c7.rect = c7.image.get_rect()

    ending = Ending()
    ending.image = content_font.render("All rights not reserved", True, color)
    ending.rect = ending.image.get_rect()

    #
    text = [t1, c1, t2, c2, t3, c3, t4, c4, t5, c5, t6, c6, t7, c7, ending]
    print("flag")

    
    x = 200
    y = 100
    for sentence in text:
        sentence.rect[0], sentence.rect[1] = x, y
        print(sentence.rect[0], sentence.rect[1])
        y += 50
    cal = 0
    while cal <= 2000:
        screen.blit(ending_bg[0], (0, 0))
        for sentence in text:
            print(sentence.rect[0], sentence.rect[1])
            sentence.rect.move_ip(0, -10)
            screen.blit(sentence.image, (sentence.rect[0], sentence.rect[1]))  
        #
        pygame.display.update()
        pygame.time.wait(1000)
        cal += 100
    ending_music.fadeout(5000)
    pygame.quit()
print('before main')
main()