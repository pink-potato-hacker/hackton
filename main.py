import Screen
import pygame


running = True
while running:
    for event in pygame.event.get(Screen.screen_func()):
        if event.type == pygame.QUIT:
            running = False

