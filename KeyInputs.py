import Consts
import Objects
import pygame

player = pygame.Rect(240, 0, Consts.PLAYER_WIDTH, Consts.PLAYER_HEIGHT)
def left_key(leftobject):
   if player.x < leftobject.x:
        player.x += Consts.VEL
def right_key(rightobject):
    if player.x <= rightobject + 4:
        player.x -= Consts.VEL

