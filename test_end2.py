import pygame
import os, sys
from pygame.locals import *
from pygame.compat import geterror


screen=pygame.display.set_mode((1250,720))
pygame.init()
clock=pygame.time.Clock()
boxx=200
boxy=200
speed = 5
image = pygame.Surface([20,20]).convert_alpha()
image.fill((255,255,255))
while True :
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            pygame.quit()
            #quit()
    image.scroll(10,10)
    screen.blit(image,((boxx + speed) % 720, (boxy + speed) % 720))
    pygame.display.update()
    clock.tick(60)