import Consts
import Objects
import pygame

player = pygame.Rect(240, 0, Consts.PLAYER_WIDTH, Consts.PLAYER_HEIGHT)
def left_key():
   if player.x > 240:
        player.x -= Consts.VEL
def right_key():
    if player.x <  260:
        player.x += Consts.VEL

