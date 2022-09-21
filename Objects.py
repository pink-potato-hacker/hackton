import pygame
import Consts
import Screen


def moving_object(object1, object2):
    object1 = pygame.Rect(100, 0, 4, 4)
    object2 = pygame.Rect(300, 0, 4, 4)
    object1.y += 10
    object2.y += 10
    return object1.y

def place_objects(object1_cords_tuple,object2_cords_tuple, png_couple):
    object1 = png_couple[0]
    object1_img = pygame.image.load("png_files/"+object1+".png")
    object1_img = pygame.transform.scale(object1_img, Consts.objects_size)
    object1 = Screen.screen.blit(object1_img, object1_cords_tuple)

    object2 = png_couple[1]
    object2_img = pygame.image.load("png_files/" + object2 + ".png")
    object2_img = pygame.transform.scale(object2_img, Consts.objects_size)
    object2 = Screen.screen.blit(object2_img, object2_cords_tuple)

    return object1,object2

