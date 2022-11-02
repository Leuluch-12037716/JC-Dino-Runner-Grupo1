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

    def update(self):
        print("Updating")

    def draw(self, screen):
        screen.blit(self.image, (50, 300))
            