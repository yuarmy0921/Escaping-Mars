import pygame, os, sys
import cv2
import numpy as np
from pygame.locals import *

class MazeBarrier(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image, self.rect = load_image("barrier.png", "main_pic")
        print(self.rect)


def main():
    pygame.init()
    screen = np.zeros((1440,800,3))
    bg = ("mars.jpg", "main_pic")
    screen.blit(bg[0], (0, 0))
    game = MazeGame()
    flag = False
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                flag = True
        if flag:
            break
    pygame.quit()

main()