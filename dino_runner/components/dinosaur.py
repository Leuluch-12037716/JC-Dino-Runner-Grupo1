import pygame

from urllib.parse import SplitResult

from dino_runner.utils.constants import RUNNING, JUMPING

from pygame.sprite import Sprite



class Dinosaur(Sprite):
    Dino_x_pos = 50
    Dino_y_pos = 300
    Initial_step = 0
    Max_step = 10
    Aceleration = 4
    Reduce_velocity = 1
    Initial_velocity = 10
    
    def __init__(self):
        self.image = RUNNING[0]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.Dino_x_pos
        self.image_rect.y = self.Dino_y_pos
        self.step = self.Initial_step 
        self.dino_jump = False
        self.dino_run = True
        self.dino_velocity = self.Initial_velocity


    def update(self, dino_event):
        if self.dino_jump:
            self.jump()
        if self.dino_run:
            self.run()

        if dino_event[pygame.K_SPACE] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
        #else:
         #   self.dino_run = True
          #  self.dino_jump = False
            

        if self.step > self.Max_step:    
            self.step = self.Initial_step

    def run(self):
        self.image = RUNNING[0] if self.step <= 5 else RUNNING[1]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.Dino_x_pos
        self.image_rect.y = self.Dino_y_pos
        self.step += 1
        

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.image_rect.y -= self.dino_velocity * self.Aceleration
            self.dino_velocity -= self.Reduce_velocity
        if self.dino_velocity < -self.Initial_velocity:
            self.image_rect.y = self.Dino_y_pos
            self.dino_jump = False
            self.dino_velocity = self.Initial_velocity
            self.dino_run = True

    def draw(self, screen):
        screen.blit(self.image, (self.image_rect.x, self.image_rect.y))
            