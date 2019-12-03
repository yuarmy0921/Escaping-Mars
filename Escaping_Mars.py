import pygame
import os, sys
from pygame.locals import *
#玩家
#pygame.mouse
def load_image(name, colorkey = None):
    pass
    '''
    把圖片載下來
    '''
    fullname = os.path.join('data', name)
def load_sound(name):
    pass

class Player(pygame.sprite.Sprite):
    '''
    隨著滑鼠移動
    碰到迷宮邊界則損血，碰到隕石也損血
    碰到NPC回血

    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image()

    def update(self):
        '''
        玩家狀態
        '''
        pos = pygame.mouse.get_pos()

    def recover(self):

    def injure(self):

class Dear(pygame.sprite.Sprite):
    '''
    寶貝們的技能
    '''
    
    
    
    




#兩個NPC
#大麥：可愛能量/


#寶貝們
#南俊：破壞/碩珍：冰凍/玧其：石化/號錫：融化/智旻：/泰亨：迷路/柾國：嗜睡



#迷宮主體
#路障
#隕石
