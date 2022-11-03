from dino_runner.components.obstaculs.obstacle import Obstacle
import random

class Cactus(Obstacle):

    def __init__(self, images):
        index = random.randint(0,2)
        super().__init__(images, index)
        self.image_rect.y = 320