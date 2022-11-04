import pygame
from dino_runner.utils.constants import SMALL_CACTUS, BIRD

from dino_runner.components.obstaculs.cactus import Cactus
from dino_runner.components.obstaculs.bird import Bird
import random


class Obstaclehandler():

    def __init__(self):
        self.obstacles = []
    
    def update(self, game): 
        if len(self.obstacles) == 0:
            C_B = random.randint(0, 1)
            if C_B == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            if C_B == 1:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed)
            if game.dinosaur.image_rect.colliderect(obstacle.image_rect):
                pygame.time.delay(300)
                self.obstacles.pop()
                game.lives -= 1


            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.pop()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen) 