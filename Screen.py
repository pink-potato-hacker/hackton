import pygame
import Consts

screen = pygame.display.set_mode(Consts.screen_size)

def screen_func():
    pygame.display.set_caption('hackton game')
    screen.fill(Consts.background_color)

