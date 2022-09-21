import pygame
import Consts


def screen_func():
    screen = pygame.display.set_mode(Consts.screen_size)
    pygame.display.set_caption('hackton game')
    screen.fill(Consts.background_color)
    pygame.display.flip()

