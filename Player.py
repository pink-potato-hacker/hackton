import Consts
import Objects
import pygame
import Screen
def player_image():
    if Consts.counter % 2 == 0:
        player_image = pygame.image.load('png_files/player_left_step.png')
        player_image = pygame.transform.scale(player_image,(90,100))
    else:
        player_image = pygame.image.load('png_files/player_right_step.png')
        player_image = pygame.transform.scale(player_image,(90, 100))
    return player_image

player = pygame.Rect(100,550, Consts.PLAYER_WIDTH, Consts.PLAYER_HEIGHT)


def left_key():
   if player.x > 100:
        player.x -= Consts.VEL


def right_key():
    if player.x <  300:
        player.x += Consts.VEL


def meeting_check(object_Y, object):
  if object_Y + 100 == 590:

      if object in Consts.sustainable_list:
          Consts.good_points += 1
      else:
          Consts.bad_points -= 1
  return Consts.good_points, Consts.bad_points
