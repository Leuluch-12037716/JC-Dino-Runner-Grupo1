from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
import pygame

FONT_STYLE = "freesansbold.ttf"
BLACK_RGB = (0, 0, 0)

def get_text_element(messege, pos_x = SCREEN_WIDTH //2, pos_y = SCREEN_HEIGHT //2, font_size = 30, font_color = BLACK_RGB):
    font = pygame.font.Font(FONT_STYLE, font_size)

    text = font.render(messege, True, font_color)
    text_rect = text.get_rect()
    text_rect.center = (pos_x, pos_y)

    return text, text_rect

