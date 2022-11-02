import pygame

from urllib.parse import SplitResult

from dino_runner.utils.constants import RUNNING

from pygame.sprite import Sprite

class Dinosaur(Sprite):
    def __init__(self):
        self.image = RUNNING[0]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = 50
        self.image_rect.y = 300
        self.step = 0 

    def update(self):
        self.image = RUNNING[0] if self.step <= 5 else RUNNING[1]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = 50
        self.image_rect.y = 300
        self.step += 1
        if self.step > 10:    
            self.step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.image_rect.x, self.image_rect.y))
            