import pygame

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
    screen = pygame.display.set_mode(1440, 800)
    bg = 
    ending_music = load_sound("magic_shop.wav")
    ending_music.play(-1)
    color = (255, 255, 255)
    title_font = pygame.font.Font.set_bold("game_material/font/HanaMin/HanaMinA.ttf", 20)
    content_font = pygame.font.Font("game_material/font/HanaMin/HanaMinA.ttf", 15)
    t1 = title_font.render("GUI Design", True, color)
    c1 = content_font.render("林郁敏", True, color)
    t2 = title_font.render("Game Configuration Construction", True, color)
    c2 = content_font.render("林郁敏", True, color)
    t3 = title_font.render("Character Design", True, color)
    c3 = content_font.render("", True, color)
    t4 = title_font.render("Character Image", True, color)
    c4 = content_font.render("BT21", True, color)
    t5 = title_font.render("Maze Design", True, color)
    c5 = content_font.render("張悅恩", True, color)
    t6 = title_font.render("Background Music", True, color)
    c6 = content_font.render("BTS-Sea     BTS-So far away     BTS-Epiphany     BTS-Magic shop     BTS-Mikrokosmos     BTS-Make it right     BTS-Tomorrow     BTS-Save ME", True, color)
    t7 = title_font.render("Special THANKS TO", True, color)
    c7 = content_font.render("林宗男 教授     ", True, color)
    ending = content_font.render("All rights not reserved", True, color)
    test = {t1:c1, t2:c2, t3:c3, t4:c4, t5:c5, t6:c6, t7:c7}
    x = 200
    y = 100
    for key, value in test:
        screen.blits(((key, (x, y)), (value, (x, y+100))))
        y += 100

    for 
    #
    ending_music.fadeout(5000)

    pygame.quit()
