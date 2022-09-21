import Screen
import pygame
import Player


running = True
while running:
    for event in pygame.event.get(Screen.screen_func()):
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Player.right_key()
            if event.key == pygame.K_LEFT:
                Player.left_key()

