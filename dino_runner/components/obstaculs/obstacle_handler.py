import pygame
from dino_runner.utils.constants import SMALL_CACTUS

from dino_runner.components.obstaculs.cactus import Cactus


class Obstaclehandler():
    def __init__(self):
        self.obstacles = []
    
    def update(self, game): 
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

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