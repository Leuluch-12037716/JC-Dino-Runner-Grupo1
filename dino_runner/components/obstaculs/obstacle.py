from dino_runner.utils.constants import SCREEN_WIDTH

from pygame.sprite import Sprite


class Obstacle(Sprite):
    def __init__(self, images ,index, x_pos = SCREEN_WIDTH):
        self.image = images[index]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = x_pos
    
    def update(self, speed):
        self.image_rect.x -= speed

    def draw(self, screen):
        screen.blit(self.image, self.image_rect)
