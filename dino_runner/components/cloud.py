from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH
from pygame.sprite import Sprite
import random

class Cloud(Sprite):
    Cloud_y_pos = [200, 150, 175, 125, 100]

    def __init__(self, x_pos = SCREEN_WIDTH):
        self.image = CLOUD
        self.image_rect = self.image.get_rect()
        self.image_rect.x = x_pos
        self.image_rect.y = self.Cloud_y_pos[random.randint(0,4)]

    
    def update(self, image):
        self.image_rect.x -= 10 
        if self.image_rect.x == 0:
            self.image_rect.x = SCREEN_WIDTH
            self.image_rect.y = self.Cloud_y_pos[random.randint(0,4)]


    def draw(self, screen): 
        screen.blit(self.image, (self.image_rect.x, self.image_rect.y))