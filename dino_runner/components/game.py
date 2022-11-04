import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

from dino_runner.components.dinosaur import Dinosaur

from dino_runner.components.obstaculs.obstacle_handler import Obstaclehandler

from dino_runner.utils import text_utils


class Game:
    Max_lives = 3
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.dinosaur = Dinosaur()
        self.obstacle_handler = Obstaclehandler()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0 
        self.lives = self.Max_lives

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        dino_event = pygame.key.get_pressed()
        self.dinosaur.update(dino_event)
        self.obstacle_handler.update(self.game_speed, self.dinosaur)
        #self.update_score()

        if self.lives == 0:
            self.playing = False

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.dinosaur.draw(self.screen)
        #self.obstacle_handler.draw(self.screen)
        #self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
         image_width = BG.get_width()
         self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
         self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
         if self.x_pos_bg <= -image_width:
             self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
             self.x_pos_bg = 0
         self.x_pos_bg -= self.game_speed

    # def draw_score(self):
    #     self.points += 1
    #     if self.points % 100 == 0: 
    #         self.game_speed += 1
    #     message = "Points: " + str(self.points)
    #     points_text, points_rect = text_utils.get_text_element(message, SCREEN_WIDTH - 100, 70 )
    #     self.screen.blit(points_text, points_rect)

    # def update_score(self):
    #     pass
        
