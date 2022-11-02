from utils.constants import RUNNING

from pygame.sprite import Sprite
class Dinosaur(Sprite):
        def __int__(self):
            self.image = RUNNING[0]
            self.image = self.image.get_part()
            self.image_rect.x = 50
            self.image_rect.y = 300

        def update(self):
            print("Updating")

        def draw(self, screen):
            screen.blit(self.image, (self.image_rect.x, self.image_rect.y))
            