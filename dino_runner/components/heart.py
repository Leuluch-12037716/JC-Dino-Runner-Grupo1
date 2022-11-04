from dino_runner.utils.constants import HEART
from pygame.sprite import Sprite
from dino_runner.utils import text_utils


class Heart(Sprite):
    Heart_x_pos = 50
    Heart_y_pos = 50

    def __init__(self):
        self.image = HEART
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.Heart_x_pos
        self.image_rect.y = self.Heart_y_pos

    
    def update(self, lives):
        self.lives = lives

    def draw(self, screen): 
        screen.blit(self.image, (self.image_rect.x, self.image_rect.y))
        black_color = (0, 0, 0)
        text, text_rect = text_utils.get_text_element(str(self.lives), self.image_rect.x + 50, self.image_rect.y + 12 , font_size= 30, font_color = black_color)
        screen.blit(text, text_rect)


        