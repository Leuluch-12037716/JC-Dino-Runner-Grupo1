from dino_runner.utils.constants import SCREEN_WIDTH

from pygame.sprite import Sprite


class Obstacle(Sprite):
    Initial_step = 0
    Max_step = 10
    def __init__(self, images ,index, moveto = False, x_pos = SCREEN_WIDTH):
        self.images = images
        self.image = images[index]
        self.moveto = moveto
        self.image_rect = self.image.get_rect()
        self.image_rect.x = x_pos
        self.step = self.Initial_step

    def update(self, speed):
        self.image_rect.x -= speed

    def draw(self, screen):
        if(self.moveto == True):
            if self.step > self.Max_step:
                self.step = self.Initial_step
            index = 0 if self.step <= 5 else 1
            self.image = self.images[index]
            self.step += 1
        screen.blit(self.image, self.image_rect)
