import time

import pygame
import Consts
import Player
from pygame import mixer

screen = pygame.display.set_mode(Consts.screen_size)


def draw_start_message(message):
    draw_message(message, Consts.START_FONT_SIZE,
    Consts.START_COLOR, Consts.START_LOCATION)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(Consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def start_screen():
    pygame.display.set_caption('hackton game')
    road = pygame.image.load('png_files/opening_screen.png')
    road = pygame.transform.scale(road, (500, 650))
    screen.blit(road, (0, 0))

def draw_hearts(bad_points):
  x = 475
  y = 0
  for i in range (bad_points):
    heart = pygame.image.load('png_files\heart.png')
    heart = pygame.transform.scale(heart, (25, 25))
    screen.blit(heart, (x, y))
    x -= 25

def draw_crowns(good_points):
  x = 0
  y = 0
  for i in range (good_points):
    crown = pygame.image.load('png_files\crown.png')
    crown = pygame.transform.scale(crown, (25, 25))
    screen.blit(crown, (x, y))
    x += 25


def draw_to_screen():
    start_screen()
    draw_hearts(Consts.bad_points)
    draw_crowns(Consts.good_points)
    screen.blit(Player.player_image(), (Player.player.x, Player.player.y))
    draw_start_message(Consts.list_info[Consts.j])
    if Consts.counter == 2:
        Consts.j = 1
    if Consts.counter == 3:
        Consts.j = 2


def load_instraction():
    pygame.display.set_caption('hackton game')
    ins = pygame.image.load('png_files\instraction.png')
    ins = pygame.transform.scale(ins, (500, 650))
    screen.blit(ins, (0, 0))
    pygame.display.update()

def lose(bad_points):
    if bad_points == 0:
        losp = pygame.image.load('png_files\lose_screen.png')
        losp = pygame.transform.scale(losp, (500, 650))
        screen.blit(losp, (0, 0))
        mixer.init()
        pop_sound = mixer.Sound("sounds/Explosion sound effect.wav")
        mixer.Sound.play(pop_sound)
        pygame.display.flip()
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        quit()
        return True
    return False

def win(good_points):
  if good_points == 5:
    winp = pygame.image.load('png_files\win.png')
    winp = pygame.transform.scale(winp, (500, 650))
    screen.blit(winp, (0, 0))
    return True
  return False

