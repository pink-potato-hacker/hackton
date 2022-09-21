import pygame

def place_objects(cords_tuple, png_couple):
    unsustainable_img = pygame.image.load("png files/injury.png")
    unsustainable_img = pygame.transform.scale(unsustainable_img, (Consts.SIZE * 2, Consts.SIZE * 4))
    Screen.screen.blit(unsustainable_img, cords_tuple)