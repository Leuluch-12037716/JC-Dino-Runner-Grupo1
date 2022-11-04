from dino_runner.components.obstaculs.obstacle import Obstacle
import random
import random
class Bird(Obstacle):
    bird_y_pos = [320, 250, 180]

    def __init__(self, images):
        index = random.randint(0,1)
        super().__init__(images, index, True)
        self.image_rect.y = self.bird_y_pos[random.randint(0,2)]