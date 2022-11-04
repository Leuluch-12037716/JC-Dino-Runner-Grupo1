from dino_runner.components.obstaculs.obstacle import Obstacle
import random

class Bird(Obstacle):

    def __init__(self, images):
        index = random.randint(0,1)
        super().__init__(images, index, True)
        self.image_rect.y = 320