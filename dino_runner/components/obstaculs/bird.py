from dino_runner.components.obstaculs.obstacle import Obstacle
import random

class Bird(Obstacle):

    def __init__(self, images):
        index = random.randint(0,1)
        super().__init__(images, index)
        self.image_rect.y = 320